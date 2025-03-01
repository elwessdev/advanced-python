import { Button, message, Modal, Table } from "antd";
import { useQuery, useQueryClient } from '@tanstack/react-query'
import axios from "axios";
import { useRef, useState } from "react";
import AddStudents from "./components/addStudents";

function App() {
    const [messageApi, contextHolder] = message.useMessage();
    const [addSudentModel, setAddStudentModel] = useState(false);
    const queryClient = useQueryClient();
    const addStudentRef = useRef(null);
    const {data:students, isLoading, error} = useQuery({
        queryFn: async () => {
            const res = await axios.get("http://127.0.0.1:8000/",{withCredentials: true});
            return res.data;
        },
        queryKey: ['studentsAPI'],
    });

    const handleAddStudent = async () =>  {
        await addStudentRef.current.submit();
    }

    const setEditStudentModel = (cin) => {
        console.log(cin);
    }

    const handleDeleteStudent = async (cin) => {
        try {
            const res = await axios.delete(`http://127.0.0.1:8000/delete/${cin}`,{withCredentials: true});
            if(res.data[1]===200){
                console.log(res);
                queryClient.invalidateQueries({queryKey: ['studentsAPI']});
            }
            if(res.data[1]===404){
                messageApi.open({
                    type: 'error',
                    content: res.data[0].message,
                });
            }
        } catch (err){
            messageApi.open({
                type: 'error',
                content: err.message,
            });
        }
    }

    return (
        <div style={{padding:"100px"}}>
            {error && (
                <div style={{color: "red"}}>
                    {error.message}
                </div>
            )}
            {contextHolder}
            <div>
                <Button type="primary" style={{marginBottom:"15px", float: "right"}} onClick={()=>setAddStudentModel(true)}>Add Student</Button>
                <Table 
                    loading={isLoading}
                    dataSource={students ? 
                        students.map((student, index) => ({
                            key: index,
                            cin: student.cin,
                            name: student.name,
                            age: student.age,
                            email: student.email,
                            phone: student.phone,
                            class: student.class,
                            options: <>
                            <Button type="primary" style={{marginRight:"7px"}} onClick={()=>setEditStudentModel(student?.cin)}>Edit</Button>
                            <Button type="primary" onClick={()=>handleDeleteStudent(student?.cin)} danger>Delete</Button>
                            </>
                        })) 
                        : []
                    } 
                    columns={[
                        {
                            title: 'CIN',
                            dataIndex: 'cin',
                            key: 'cin',
                        },
                        {
                            title: 'Name',
                            dataIndex: 'name',
                            key: 'name',
                        },
                        {
                            title: 'Age',
                            dataIndex: 'age',
                            key: 'age',
                        },
                        {
                            title: 'Email',
                            dataIndex: 'email',
                            key: 'email',
                        },
                        {
                            title: 'Phone',
                            dataIndex: 'phone',
                            key: 'phone',
                        },
                        {
                            title: 'Class',
                            dataIndex: 'class',
                            key: 'class',
                        },
                        {
                            title: 'Options',
                            dataIndex: 'options',
                            key: 'options',
                        }
                    ]}
                />
            </div>
            {/* Add Student */}
            <Modal
                title="Basic Modal"
                open={addSudentModel} 
                onOk={handleAddStudent}
                onCancel={()=>setAddStudentModel(false)} 
                okText="Add Student"
            >
                <AddStudents 
                    addRef={addStudentRef} 
                    setAddStudentModel={setAddStudentModel}
                />
            </Modal>
        </div>
    )
}

export default App
