import { Button, message, Modal, Table } from "antd";
import { useQuery, useQueryClient } from '@tanstack/react-query'
import axios from "axios";
import { useRef, useState } from "react";
import StudentForm from "./components/studentForm";

function App() {
    const [messageApi, contextHolder] = message.useMessage();
    const queryClient = useQueryClient();
    
    // Get Students
    const {data:students, isLoading, error} = useQuery({
        queryFn: async () => {
            const res = await axios.get("http://127.0.0.1:8000/");
            return res.data;
        },
        queryKey: ['studentsAPI'],
    });

    // Add Student
    const [addSudentModel, setAddStudentModel] = useState(false);
    const addStudentRef = useRef(null);
    const handleAddStudent = async () =>  {
        await addStudentRef.current.submit();
    }

    // Delete Student
    const handleDeleteStudent = async (cin) => {
        try {
            const res = await axios.delete(`http://127.0.0.1:8000/delete/${cin}`);
            if(res.data[1]===200){
                // console.log(res);
                messageApi.open({
                    type: 'success',
                    content: res.data[0].message,
                });
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

    // Edit Student
    const editStudentRef = useRef(null);
    const [editStudentModel, setEditStudentModel] = useState(false);
    const [editStudentData, setEditStudentData] = useState(null);
    const handleOpenEditStudent = async(cin) => {
        try {
            const res = await axios.get(`http://127.0.0.1:8000/info/${cin}`);
            if(res.data[1]===404){
                messageApi.open({
                    type: 'error',
                    content: res.data[0].message,
                });
                return;
            }
            if(res.data[1]==200){
                setEditStudentData(res.data[0]);
                setEditStudentModel(true);
            }
        } catch (err){
            messageApi.open({
                type: 'error',
                content: "Sudent Info not found",
            });
        }
        setEditStudentModel(true);
    }
    const handleEditStudent = () => {
        editStudentRef.current.submit();
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
                            class: student.class_s,
                            options: <>
                                <Button type="primary" style={{marginRight:"7px"}} onClick={()=>handleOpenEditStudent(student?.cin)}>Edit</Button>
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
                title="Add Student"
                open={addSudentModel} 
                onOk={handleAddStudent}
                onCancel={()=>setAddStudentModel(false)} 
                okText="Add Student"
            >
                <StudentForm 
                    type="add"
                    FormRef={addStudentRef} 
                    modelStatus={setAddStudentModel}
                    data={[]}
                />
            </Modal>
            {/* Edit Student */}
            <Modal
                title="Edit Student"
                open={editStudentModel} 
                onOk={handleEditStudent}
                onCancel={()=>setEditStudentModel(false)} 
                okText="Save"
            >
                <StudentForm
                    type="edit"
                    FormRef={editStudentRef}
                    modelStatus={setEditStudentModel}
                    data={editStudentData}
                />
            </Modal>
        </div>
    )
}

export default App
