import axios from "axios";
import { Form, Input, Button, Card, message } from "antd";
import { useForm } from "antd/es/form/Form";
import { useImperativeHandle } from "react";

export default function AddStudents({addRef}) {
    const [messageApi, contextHolder] = message.useMessage();
    const [form] = useForm();

    const handleSubmit = async (values) => {
        console.log(values);
        try {
            const res = await axios.post("http://127.0.0.1:8000/add/", values, {
                withCredentials: true,
            });
            console.log(res);
            if(res.status==200){
                messageApi.open({
                    type: 'success',
                    content: res.data.message,
                });
            }
        } catch (err) {
            console.log(err);
        }
    };

    useImperativeHandle(addRef,handleSubmit,[addRef]);
    return (
        <>
        {contextHolder}
        <Form
            form={form}
            layout="vertical"
            onFinish={handleSubmit}
        >
            <Form.Item
                label="Cin"
                name="cin"
                rules={[{ required: true, message: "Please enter your cin" }]}
            >
                <Input name="cin" />
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
                rules={[{ required: true, message: "Please enter your email" }]}
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
