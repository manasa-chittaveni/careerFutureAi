from fastapi.testclient import TestClient

from src.app.main import app


client = TestClient(app)


def test_health():

    response = client.get(
        "/health"
    )

    assert response.status_code == 200

    assert (
        response.json()["status"]
        == "healthy"
    )


def test_prediction():

    payload = {
        "python": 5,
        "sql": 5,
        "machine_learning": 4,
        "deep_learning": 3,
        "statistics": 4,
        "data_preprocessing": 4,
        "model_evaluation": 4,
        "dsa": 4,
        "java": 2,
        "spring_boot": 1,
        "javascript": 2,
        "react": 2,
        "nodejs": 1,
        "docker": 3,
        "linux": 2,
        "kubernetes": 1,
        "cloud": 3,
        "aws": 3,
        "nlp": 3,
        "pytorch": 4,
        "tensorflow": 4,
        "projects": 7,
        "internships": 1,
        "experience_years": 1,
        "learning_hours_per_week": 18,
        "certifications": 3,
        "github_projects": 6
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

    body = response.json()

    assert "predictions" in body