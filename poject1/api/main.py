from typing import Union
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Cors Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:5173/",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

students = []

# Get All Students Route
@app.get("/")
def get_students():
    return students

# Add Student Route
@app.post("/add/")
def add_student(student: dict):
    # print(student["cin"])
    if student not in students and student["cin"] not in [s["cin"] for s in students]:
        students.append(student)
        return {"message": "Student Added Successfully"}, status.HTTP_201_CREATED
    else:
        return {"message": "Student Already Exists"}, status.HTTP_400_BAD_REQUEST
    
# Delete Student Route
@app.delete("/delete/{cin}")
def delete_student(cin: str):
    for student in students:
        if student["cin"] == cin:
            students.remove(student)
            return {"message": "Student Deleted Successfully"}, status.HTTP_200_OK
    return {"message": "Student Not Found"}, status.HTTP_404_NOT_FOUND

# Get Student By CIN Route
@app.get("/info/{cin}")
def get_student_info(cin:str):
    print(cin)
    for student in students:
        if student["cin"]==cin:
            return student, status.HTTP_200_OK
    return {"message": "Student Not Found"}, status.HTTP_404_NOT_FOUND

# Edit Student Route
@app.put("/edit/{cin}")
def edit_student(cin:str,data:dict):
    print(cin)
    for student in students:
        if student["cin"]==cin:
            student.update(data)
            return {"message": "Student Updated Successfully"}, status.HTTP_200_OK
    return {"message": "Student Not Found"}, status.HTTP_404_NOT_FOUND