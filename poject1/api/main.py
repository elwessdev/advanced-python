# from typing import Union, Optional
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
# from bson import ObjectId
from database import db


app = FastAPI()
# Cors Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:5173/",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB Config
studentCollection = db["students"]
class Student(BaseModel):
    cin: str
    name: str
    age: str
    email: str
    phone: str
    class_s: str

# students = []

# Get All Students Route
@app.get("/")
async def get_students():
    students = await studentCollection.find().to_list(length=None)
    for student in students:
        student["_id"] = str(student["_id"])
async def get_students():
    students = await studentCollection.find().to_list(length=None)
    for student in students:
        student["_id"] = str(student["_id"])
    return students



# Add Student Route
@app.post("/add/")
async def add_student(student: Student):
    print(student.dict())
    check = await studentCollection.find_one({"cin": student.cin})
    if check:
        return {"message": "Student Already Exists"}, status.HTTP_400_BAD_REQUEST
    else:
        await studentCollection.insert_one(student.dict())
async def add_student(student: Student):
    print(student.dict())
    check = await studentCollection.find_one({"cin": student.cin})
    if check:
        return {"message": "Student Already Exists"}, status.HTTP_400_BAD_REQUEST
    else:
        await studentCollection.insert_one(student.dict())
        return {"message": "Student Added Successfully"}, status.HTTP_201_CREATED
    

    

# Delete Student Route
@app.delete("/delete/{cin}")
async def delete_student(cin: str):
    delRe = await studentCollection.delete_one({"cin": cin})
    if delRe.deleted_count:
        return {"message": "Student Deleted Successfully"}, status.HTTP_200_OK
async def delete_student(cin: str):
    delRe = await studentCollection.delete_one({"cin": cin})
    if delRe.deleted_count:
        return {"message": "Student Deleted Successfully"}, status.HTTP_200_OK
    return {"message": "Student Not Found"}, status.HTTP_404_NOT_FOUND



# Get Student By CIN Route
@app.get("/info/{cin}")
async def get_student_info(cin:str):
    infos = await studentCollection.find_one({"cin": cin})
    if infos:
        infos["_id"] = str(infos["_id"])
        return infos, status.HTTP_200_OK
async def get_student_info(cin:str):
    infos = await studentCollection.find_one({"cin": cin})
    if infos:
        infos["_id"] = str(infos["_id"])
        return infos, status.HTTP_200_OK
    return {"message": "Student Not Found"}, status.HTTP_404_NOT_FOUND



# Edit Student Route
@app.put("/edit/{cin}")
async def edit_student(cin:str,data: dict):
    student = await studentCollection.find_one_and_update({"cin": cin}, {"$set": data})
    if student:
        return {"message": "Student Updated Successfully"}, status.HTTP_200_OK
    return {"message": "Student Not Found"}, status.HTTP_404_NOT_FOUND