from pydantic import BaseModel

class Weather(BaseModel):
    city: str
    temperature: float
    description: str
    humidity: int
    wind_speed: float
    icon: str
    timestamp: str