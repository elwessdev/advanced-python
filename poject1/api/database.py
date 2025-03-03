from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

# MONGO_URI = "mongodb+srv://ruut:ruut+2018@cluster0.m220b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = AsyncIOMotorClient("mongodb://127.0.0.1:27017", server_api=ServerApi('1'))
db = client["FastAPI_SMS"]