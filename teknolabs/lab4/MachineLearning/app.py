from fastapi import FastAPI
from pydantic import BaseModel
import joblib

model = joblib.load('music_recommender.joblib')

app = FastAPI(title="Music Recommender API")

class UserInput(BaseModel):
    age: int
    gender: int 

@app.post("/predict")
def predict(user_input: UserInput):
    data = [[user_input.age, user_input.gender]]
    prediction = model.predict(data)
    return {"genre": prediction[0]}
