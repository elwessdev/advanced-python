from typing import Union
from fastapi import FastAPI
# import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:5173/",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


students = [
    {
        "cin": "123456",
        "name": "iyadh",
        "age": 20,
        "email": "test@test.com",
        "phone": "12345678",
        "class": "DSI21"
    },
    {
        "cin": "123456",
        "name": "iyadh",
        "age": 20,
        "email": "test@test.com",
        "phone": "12345678",
        "class": "DSI21"
    },
    {
        "cin": "123456",
        "name": "iyadh",
        "age": 20,
        "email": "test@test.com",
        "phone": "12345678",
        "class": "DSI21"
    },
]

# Get Students Route
@app.get("/")
def get_students():
    print(students)
    return students

# Post Student Route
@app.post("/add/")
def add_student(student: dict):
    students.append(student)
    return {"message": "done"}