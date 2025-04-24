from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: EmailStr

users = [
    {
        "id": 7,
        "name": "Osama",
        "email": "aa@aa.com"
    },
    {
        "id": 8,
        "name": "Ali",
        "email": "osama@osama.com"
    }
]

@app.get("/")
def read_root():
    return users

# @app.get("/user/{userID}")
# def getUser(userID: int) -> str:
#     if userID==1:
#         return "workss bo7"
#     else:
#         raise HTTPException(status_code=404, detail="user not found y broo")
    
@app.get("/user/{userID}", response_model=User)
def getUser(userID: int) -> str:
    if userID <= len(users):
        return users[userID-1]
    else:
        raise HTTPException(status_code=404, detail="user not found y broo")