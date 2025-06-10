from fastapi import FastAPI, Request
from pydantic import BaseModel
import random
import datetime

app = FastAPI()

class PredictionRequest(BaseModel):
    claim_id: int
    amount: float

@app.get("/")
async def root():
    return {"message": "Dummy ML Model with FastAPI is running!"}

@app.post("/predict")
async def predict(request: PredictionRequest):
    prediction = random.choice(["Fraud", "Valid"])
    result = {
        "claim_id": request.claim_id,
        "amount": request.amount,
        "prediction": prediction,
        "confidence": random.uniform(0.5, 1.0),  # Simulated confidence score
        "model_version": "1.0.0",  # Simulated model version
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",  # Simulated timestamp
        "explanation": "This is a simulated explanation for the prediction.",  # Simulated explanation
        "additional_info": {
            "feature_importance": {
                "amount": random.uniform(0.1, 0.5),
                "claim_id": random.uniform(0.1, 0.5)
            },
            "model_metadata": {
                "training_data_size": 10000,
                "training_data_version": "v1.0"
            }
        },
        "model_name": "dummy_fraud_detection_model",  # Simulated model name
        "model_type": "classification",  # Simulated model type
        "input_features": {
            "claim_id": request.claim_id,
            "amount": request.amount
        },
        "output_labels": ["Fraud", "Valid"],  # Simulated output labels
        "prediction_time": datetime.datetime.utcnow().isoformat() + "Z",  # Simulated prediction time
        "model_accuracy": random.uniform(0.7, 0.95),  # Simulated model accuracy
        "model_performance": {
            "precision": random.uniform(0.7, 0.95),
            "recall": random.uniform(0.7, 0.95),
            "f1_score": random.uniform(0.7, 0.95)
        },
        "model_training_info": {
            "training_duration": "PT1H",  # Simulated training duration in ISO 8601 format
            "training_algorithm": "RandomForestClassifier"  # Simulated training algorithm
        }

    }
    return {
        "input_data": request.model_dump(),
        "prediction": result
    }

