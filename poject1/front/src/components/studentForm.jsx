import axios from "axios";
import { Form, Input, Button, Card, message } from "antd";
import { useForm } from "antd/es/form/Form";
import { useQueryClient } from "@tanstack/react-query";
import { memo, useEffect } from "react";

export const StudentForm = ({type,FormRef,modelStatus,data})=>{
    const [messageApi, contextHolder] = message.useMessage();
    const queryClient = useQueryClient();
    const [form] = useForm();

    useEffect(() => {
        // console.log(data,type);
        form.setFieldsValue({
            cin: data&&type=="edit" ? data?.cin : null,
            name: data&&type=="edit" ? data?.name : null,
            age: data&&type=="edit" ? data?.age : null,
            email: data&&type=="edit" ? data?.email : null,
            phone: data&&type=="edit" ? data?.phone : null,
            class: data&&type=="edit" ? data?.class : null,
        });
    }, [data,type,form]);

    const handleAddStudent = async (values) => {
        // console.log(values);
        try {
            const res = await axios.post("http://127.0.0.1:8000/add/", values);
            // console.log(res);
            if(res.data[1]==201){
                queryClient.invalidateQueries({queryKey: ['studentsAPI']});
                messageApi.open({
                    type: 'success',
                    content: res.data[0].message,
                });
                modelStatus(false);
            }
            if (res.data[1] == 400) {
                messageApi.open({
                    type: 'error',
                    content: res.data[0].message,
                });
            }
        } catch (err) {
            console.log(err);
        }
    };

    const handleEditStudent = async (values) => {
        if(values.cin==data.cin){
            let newData = {};
            for (let key in values) {
                if (key!=="cin"&&values[key]!==data[key]) {
                    newData[key] = values[key];
                }
            }
            if(Object.entries(newData).length>0){
                try{
                    const res = await axios.put(`http://127.0.0.1:8000/edit/${data.cin}`, newData);
                    if(res.data[1]==200){
                        queryClient.invalidateQueries({queryKey: ['studentsAPI']});
                        modelStatus(false);
                        messageApi.open({
                            type: 'success',
                            content: res.data[0].message,
                        });
                    }
                    if (res.data[1]==404) {
                        messageApi.open({
                            type: 'error',
                            content: res.data[0].message,
                        });
                    }
                } catch(err){
                    messageApi.open({
                        type: 'error',
                        content: err.message,
                    });
                }
            }
        }
    };

    return (
        <>
        {contextHolder}
        <Form
            ref={FormRef}
            form={form}
            layout="vertical"
            onFinish={type=="add" ?handleAddStudent :handleEditStudent}
        >
            <Form.Item
                label="Cin"
                name="cin"
                rules={[{ required: true, message: "Please enter your cin" }]}
            >
                <Input name="cin" disabled={type=="edit"} />
            </Form.Item>
            <Form.Item
                label="Name"
                name="name"
                rules={[{ required: true, message: "Please enter your name" }]}
            >
                <Input name="name" />
            </Form.Item>
            <Form.Item
                label="Age"
                name="age"
                rules={[{ required: true, message: "Please enter your age" }]}
            >
                <Input type="number" name="age" />
            </Form.Item>
            <Form.Item
                label="Email"
                name="email"
                rules={[
                    { required: true, message: "Please enter your email" },
                    { type: 'email', message: 'The input is not valid E-mail!' }
                ]}
            >
                <Input name="email" />
            </Form.Item>
            <Form.Item
                label="Phone"
                name="phone"
                rules={[{ required: true, message: "Please enter your phone" }]}
            >
                <Input type="number" name="phone" />
            </Form.Item>
            <Form.Item
                label="Class"
                name="class"
                rules={[{ required: true, message: "Please enter your class" }]}
            >
                <Input name="class" />
            </Form.Item>
        </Form>
        </>
    );
}
export default memo(StudentForm);