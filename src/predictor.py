from pathlib import Path

import joblib
import pandas as pd


# ---------------------------------------------------------
# MODEL DIRECTORY
# ---------------------------------------------------------

MODEL_DIR = Path(__file__).resolve().parent / "models"


# ---------------------------------------------------------
# ROLE -> MODEL FILE
# ---------------------------------------------------------

ROLE_MODELS = {

    "ML Engineer":
        "ml_engineer_ready.joblib",

    "Data Scientist":
        "data_scientist_ready.joblib",

    "Data Analyst":
        "data_analyst_ready.joblib",

    "Backend Developer":
        "backend_developer_ready.joblib",

    "AI Engineer":
        "ai_engineer_ready.joblib",

    "DevOps Engineer":
        "devops_engineer_ready.joblib"
}


# ---------------------------------------------------------
# LOAD ALL TRAINED MODELS
# ---------------------------------------------------------

def load_models():

    models = {}

    for role, filename in ROLE_MODELS.items():

        model_path = MODEL_DIR / filename

        if not model_path.exists():

            raise FileNotFoundError(
                f"Model not found: {model_path}"
            )

        artifact = joblib.load(
            model_path
        )

        models[role] = artifact

    return models


MODELS = load_models()


# ---------------------------------------------------------
# PREDICT FOR ALL ROLES
# ---------------------------------------------------------

def predict_all_roles(candidate: dict):

    results = {}


    for role, artifact in MODELS.items():

        model = artifact["model"]

        features = artifact["features"]


        # Convert dictionary -> DataFrame

        input_df = pd.DataFrame(
            [candidate]
        )


        # IMPORTANT:
        # use exactly the same feature order
        # that was used during training

        input_df = input_df[
            features
        ]


        # Get probability of class 1

        probability = (
            model.predict_proba(
                input_df
            )[0, 1]
        )


        # Convert probability to binary decision

        ready = int(
            probability >= 0.50
        )


        results[role] = {

            "probability": round(
                float(probability),
                4
            ),

            "percentage": round(
                float(probability * 100),
                2
            ),

            "ready": ready,

            "model_version":
                artifact["version"]
        }


    return results