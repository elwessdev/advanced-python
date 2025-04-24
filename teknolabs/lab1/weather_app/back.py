from pydantic import BaseModel
import requests as req
from fastapi import FastAPI

# Models
class WeatherRequest(BaseModel):
    city: str

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    description: str


#  FastAPI
app = FastAPI()


@app.get("/")
def root():
    return "Server works!!"

@app.post("/weather", response_model=WeatherResponse)
def get_weather(data: WeatherRequest):
    try:
        res = req.get("http://api.openweathermap.org/data/2.5/weather",{
            "q": data.city,
            "appid": "f44af96718edd14bb8a7006ab45b2ae3",
            "units": "metric"
        })
        res_json = res.json()
        return {
            "city": data.city,
            "temperature": res_json["main"]["temp"],
            "description": res_json["weather"][0]["description"]
        }
    except Exception as e:
        return {"error": str(e)}