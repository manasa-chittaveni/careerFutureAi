# CareerFuture AI 🚀

CareerFuture AI is an end-to-end machine learning project that predicts **role-wise career readiness** from a candidate's skills, experience, projects, learning activity, and other profile information.

The project is designed as a practical learning project covering:

- Data preparation and exploratory analysis
- Supervised machine learning with Random Forest
- Multi-role prediction
- Model evaluation
- Skill-gap analysis
- FastAPI deployment
- Automated API testing
- Git/GitHub workflow
- MLflow and MLOps (next stage)
- Cloud deployment (next stage)
- Docker (next stage)
- Future extensions such as deep learning, NLP, LLMs, and RAG

> **Important:** The current dataset is synthetic and is intended for learning and system development. The prediction values are not real hiring probabilities and should not be interpreted as guaranteed career outcomes.

---

## 🎯 Project Objective

The goal of CareerFuture AI is to build a system that takes a candidate profile and produces readiness estimates for multiple technical career roles.

Currently supported roles:

1. ML Engineer
2. Data Scientist
3. Data Analyst
4. Backend Developer
5. AI Engineer
6. DevOps Engineer

For each role, the API returns:

- Readiness probability
- Readiness percentage
- Ready/not-ready indicator based on the configured threshold
- Model version
- Skill gaps for the role

---

## 🏗️ Architecture

```text
Candidate Profile
       ↓
Pydantic Validation
       ↓
FastAPI
       ↓
Prediction Engine
       ↓
6 Role-Specific Random Forest Models
       ↓
Role Readiness Predictions
       ↓
Skill Gap Analysis
       ↓
JSON API Response
```

### Current ML pipeline

```text
Synthetic Dataset
      ↓
Train / Validation / Test Split
      ↓
Preprocessing
      ↓
Random Forest Classifier
      ↓
Evaluation
      ↓
.joblib Model Artifacts
      ↓
FastAPI Prediction API
```

---

## 📁 Project Structure

```text
careerFutureAi/
│
├── .gitignore
├── requirements.txt
├── test_api.py
│
└── src/
    ├── app/
    │   ├── main.py
    │   └── schemas.py
    │
    ├── models/
    │   ├── ai_engineer_ready.joblib
    │   ├── backend_developer_ready.joblib
    │   ├── data_analyst_ready.joblib
    │   ├── data_scientist_ready.joblib
    │   ├── devops_engineer_ready.joblib
    │   ├── ml_engineer_ready.joblib
    │   └── model_metrics.csv
    │
    ├── predictor.py
    ├── skill_gap.py
    ├── train.py
    ├── test_prediction.py
    └── career_multi_role.csv
```

---

## 🧰 Technologies Used

### Machine Learning

- Python
- NumPy
- Pandas
- Scikit-learn
- Random Forest
- Joblib

### API

- FastAPI
- Pydantic
- Uvicorn

### Testing

- Pytest
- HTTPX

### Version Control

- Git
- GitHub

### Planned MLOps / Deployment

- MLflow
- Docker
- GitHub Actions / CI/CD
- Render or another cloud platform

---

## 📊 Features Used by the Model

The current dataset contains candidate attributes such as:

- Python
- SQL
- Machine Learning
- Deep Learning
- Statistics
- Data Preprocessing
- Model Evaluation
- DSA
- Java
- Spring Boot
- JavaScript
- React
- Node.js
- Docker
- Linux
- Kubernetes
- Cloud
- AWS
- NLP
- PyTorch
- TensorFlow
- Projects
- Internships
- Experience
- Learning Hours per Week
- Certifications
- GitHub Projects

Most skill values use a **0–5 proficiency scale**.

---

## 🤖 Machine Learning Approach

CareerFuture AI uses **six separate binary Random Forest classifiers**.

Each model predicts whether a candidate is ready for one specific role:

```text
Candidate Features
       ↓
 ┌───────────────────────────────┐
 │ ML Engineer Model             │
 │ Data Scientist Model          │
 │ Data Analyst Model            │
 │ Backend Developer Model       │
 │ AI Engineer Model             │
 │ DevOps Engineer Model         │
 └───────────────────────────────┘
       ↓
Role-wise probabilities
```

The models are independent. A candidate can therefore receive high readiness estimates for more than one role.

### Random Forest configuration

The current training pipeline uses parameters including:

```text
n_estimators = 300
max_depth = 12
min_samples_split = 5
min_samples_leaf = 2
max_features = sqrt
class_weight = balanced
random_state = 42
```

Missing numeric values are handled with median imputation inside the model pipeline.

---

## 📈 Model Evaluation

The training process evaluates each role-specific model using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

The metrics are stored in:

```text
src/models/model_metrics.csv
```

Because the current dataset is synthetic, these metrics demonstrate the ML pipeline rather than real-world hiring performance.

---

## 🧠 Skill Gap Analysis

The skill-gap engine compares a candidate's current proficiency against role-specific expected proficiency.

Example:

```text
Required Python: 4/5
Candidate Python: 2/5

Skill Gap: 2 levels
```

This allows the API to provide actionable information about skills that can be developed for a selected role.

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/manasa-chittaveni/careerFutureAi.git
cd careerFutureAi
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv ml_env
.\ml_env\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

## ▶️ Run the API

From the project root:

```powershell
uvicorn src.app.main:app --reload
```

The API will normally start at:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Health endpoint:

```text
http://127.0.0.1:8000/health
```

---

## 🔍 API Endpoints

### GET `/health`

Checks whether the API is running.

Example response:

```json
{
  "status": "healthy",
  "service": "CareerFuture AI",
  "version": "1.0.0"
}
```

### POST `/predict`

Accepts a candidate profile and returns role-wise readiness predictions and skill gaps.

The easiest way to test it is through Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## 🧪 Run Tests

Run all tests from the project root:

```powershell
pytest
```

Current test status:

```text
2 passed
```

The tests validate important parts of the API/model workflow.

---

## 🧑‍💻 Training the Models

To retrain the six role-specific models, run the training script using the project's environment.

From the project root:

```powershell
python src/train.py
```

The generated model artifacts are written to:

```text
src/models/
```

---

## 🔄 MLOps Roadmap

The project is being developed progressively toward a production-style ML system.

```text
Data
 ↓
Model Training
 ↓
Evaluation
 ↓
Model Artifacts
 ↓
FastAPI
 ↓
Automated Tests
 ↓
Git / GitHub
 ↓
MLflow Tracking
 ↓
Model Registry
 ↓
CI/CD
 ↓
Cloud Deployment
 ↓
Monitoring
 ↓
Drift Detection
 ↓
Retraining
```

### Planned MLflow usage

MLflow will be used to track:

- Experiments
- Parameters
- Metrics
- Artifacts
- Model versions
- Model lineage
- Deployment aliases such as `champion`

---

## 🐳 Docker Roadmap

Docker will later package the API, Python runtime, dependencies, and model artifacts into a reproducible container image.

```text
FastAPI + Models + Dependencies
              ↓
         Docker Image
              ↓
           Container
```

Docker is not required for the current local API workflow and can be added as a later deployment stage.

---

## ☁️ Deployment Roadmap

The first direct cloud deployment can use a native Python web service.

Example production start command:

```text
uvicorn src.app.main:app --host 0.0.0.0 --port $PORT
```

The intended deployment flow is:

```text
GitHub Repository
       ↓
Cloud Build
       ↓
Install requirements.txt
       ↓
Start Uvicorn
       ↓
FastAPI API
       ↓
Public HTTPS Endpoint
```

---

## 🚀 Future Development

CareerFuture AI is intended to grow beyond the first Random Forest version.

### Phase 1 — Current

- Multi-role tabular ML
- Random Forest
- Skill-gap analysis
- FastAPI
- Testing
- Git/GitHub

### Phase 2 — MLOps

- MLflow experiment tracking
- Model Registry
- Model versioning
- CI/CD
- Cloud deployment
- Monitoring
- Data/model drift detection
- Automated retraining

### Phase 3 — Deep Learning

- Neural Networks / MLP
- Model comparison and ensembles
- CNN/Conv1D for suitable forecasting tasks
- LSTM/time-series forecasting where appropriate

### Phase 4 — AI Engineering

- NLP
- Resume and job-description processing
- Transformers
- Embeddings
- Vector databases
- LLMs
- Retrieval-Augmented Generation (RAG)
- AI agents

### Phase 5 — Full Product

A future web application can provide:

```text
User Profile
    ↓
CareerFuture AI Backend
    ↓
ML Predictions + Skill Gaps
    ↓
Future Skill Demand Forecasting
    ↓
LLM / RAG Career Guidance
    ↓
Interactive Web Dashboard
```

---

## ⚠️ Limitations

The current version is a learning and engineering prototype.

- The dataset is synthetic.
- Predictions are model estimates, not guaranteed career outcomes.
- Real hiring decisions depend on many factors that are not represented here.
- Model performance on synthetic data does not establish performance on real-world employment data.
- A production system would require carefully sourced, representative, and legally/ethically reviewed data.

---

## 👩‍💻 Author

**Chittaveni Manasa**

Computer Science Engineering Student

GitHub: https://github.com/manasa-chittaveni

---

## 📄 License

This project is currently intended for educational and portfolio use.
