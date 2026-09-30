from predictor import predict_all_roles


candidate = {

    "python": 5,
    "sql": 5,

    "machine_learning": 5,
    "deep_learning": 4,

    "statistics": 4,

    "data_preprocessing": 5,
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


results = predict_all_roles(
    candidate
)


print("\nCAREERFUTURE PREDICTIONS")
print("=" * 60)


for role, result in results.items():

    print(
        f"{role:25} "
        f"{result['percentage']:6.2f}%"
    )