from fastapi import FastAPI, Depends, HTTPException, Header
import ollama
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_CREDITS = {API_KEY: 5}

def verify_api_key(x_api_key: str = Header(None)):
    credits = API_KEY_CREDITS.get(x_api_key, 0)
    if credits <= 0:
        raise HTTPException(status_code=401, detail="Invalid API Key or No Credits")
    return x_api_key

@app.post("/generate")
def generate(prompt: str, api_key: str = Depends(verify_api_key)):
    API_KEY_CREDITS[api_key] -= 1
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return {"response": response["message"]["content"]}
