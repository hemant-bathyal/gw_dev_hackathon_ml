from fastapi import FastAPI, Request
from pydantic import BaseModel
import random

app = FastAPI()

class PredictionRequest(BaseModel):
    claim_id: int
    amount: float

@app.get("/")
async def root():
    return {"message": "Dummy ML Model with FastAPI is running!"}

@app.post("/predict")
async def predict(request: PredictionRequest):
    prediction = random.choice(["Approved", "Denied"])
    return {
        "input_data": request.model_dump(),
        "prediction": prediction
    }


# uvicorn main:app --host 0.0.0.0 --port 8080 --reload
