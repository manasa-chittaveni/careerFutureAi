from pydantic import BaseModel, Field


class CandidateRequest(BaseModel):

    python: float = Field(ge=0, le=5)
    sql: float = Field(ge=0, le=5)

    machine_learning: float = Field(
        ge=0,
        le=5
    )

    deep_learning: float = Field(
        ge=0,
        le=5
    )

    statistics: float = Field(
        ge=0,
        le=5
    )

    data_preprocessing: float = Field(
        ge=0,
        le=5
    )

    model_evaluation: float = Field(
        ge=0,
        le=5
    )

    dsa: float = Field(
        ge=0,
        le=5
    )

    java: float = Field(
        ge=0,
        le=5
    )

    spring_boot: float = Field(
        ge=0,
        le=5
    )

    javascript: float = Field(
        ge=0,
        le=5
    )

    react: float = Field(
        ge=0,
        le=5
    )

    nodejs: float = Field(
        ge=0,
        le=5
    )

    docker: float = Field(
        ge=0,
        le=5
    )

    linux: float = Field(
        ge=0,
        le=5
    )

    kubernetes: float = Field(
        ge=0,
        le=5
    )

    cloud: float = Field(
        ge=0,
        le=5
    )

    aws: float = Field(
        ge=0,
        le=5
    )

    nlp: float = Field(
        ge=0,
        le=5
    )

    pytorch: float = Field(
        ge=0,
        le=5
    )

    tensorflow: float = Field(
        ge=0,
        le=5
    )

    projects: int = Field(
        ge=0
    )

    internships: int = Field(
        ge=0
    )

    experience_years: float = Field(
        ge=0
    )

    learning_hours_per_week: float = Field(
        ge=0
    )

    certifications: int = Field(
        ge=0
    )

    github_projects: int = Field(
        ge=0
    )