import { Button, message, Modal, Table } from "antd";
import axios from "axios";
import { useEffect, useRef, useState } from "react";
import AddStudents from "./components/addStudents";

function App() {
const [students, setStudents] = useState([]);
    const [messageApi, contextHolder] = message.useMessage();
    const [isLoading, setIsLoading] = useState(false);

    useEffect(()=>{
        const getStudents = async()=>{
            setIsLoading(true);
            try {
                const res = await axios.get("http://127.0.0.1:8000/",{
                    withCredentials: true,
                });
                setStudents(res.data);
                console.log(res);
            } catch (err){
                messageApi.open({
                    type: 'error',
                    content: `get students error: ${err}`,
                });
            } finally {
                setIsLoading(false);
            }
        }
        getStudents();
        return () => {
            getStudents();
        }
    },[]);

    // Add Student
    const [studentModel, setStudentModel] = useState(false);
    const addStudentRef = useRef(null);
    const handleAddStudent = () =>  {
      messageApi.loading('Action in progress..', 2.5);
      console.log(addStudentRef);
    }

    return (
        <div style={{padding:"100px"}}>
            {contextHolder}
            <div>
              <Button type="primary" style={{marginBottom:"15px", float: "right"}}>Add Student</Button>
                <Table 
                  loading={isLoading}
                  dataSource={
                      students.map((student, index) => ({
                          key: index,
                          cin: student.cin,
                          name: student.name,
                          age: student.age,
                          email: student.email,
                          phone: student.phone,
                          class: student.class,
                          options: <>
                            <Button type="primary" style={{marginRight:"7px"}} onClick={()=>setStudentModel(true)}>Edit</Button>
                            <Button type="primary" danger>Delete</Button>
                          </>
                      }))
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
              open={studentModel} 
              onOk={handleAddStudent}
              onCancel={()=>setStudentModel(false)} 
              okText="Add Student"
            >
              <AddStudents addRef={addStudentRef} />
            </Modal>
        </div>
    )
}

export default App
