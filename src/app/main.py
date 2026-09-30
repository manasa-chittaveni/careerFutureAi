from fastapi import FastAPI

from .schemas import CandidateRequest

from ..predictor import predict_all_roles
from ..skill_gap import calculate_skill_gaps


app = FastAPI(
    title="CareerFuture AI",
    description="Multi-role career readiness prediction API",
    version="1.0.0"
)


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "CareerFuture AI",
        "version": "1.0.0"
    }


@app.post("/predict")
def predict(candidate: CandidateRequest):

    data = candidate.model_dump()

    predictions = predict_all_roles(data)

    for role in predictions:

        predictions[role]["skill_gaps"] = calculate_skill_gaps(
            data,
            role
        )

    return {
        "service": "CareerFuture AI",
        "predictions": predictions
    }