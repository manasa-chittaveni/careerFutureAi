from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


# ============================================================
# CONFIGURATION
# ============================================================

DATA_PATH = Path(
    "career_mult_role.csv"
)

MODEL_DIR = Path("models")
MODEL_DIR.mkdir(
    parents=True,
    exist_ok=True
)


TARGET_COLUMNS = [
    "ml_engineer_ready",
    "data_scientist_ready",
    "data_analyst_ready",
    "backend_developer_ready",
    "ai_engineer_ready",
    "devops_engineer_ready",
]


# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv("career_multi_role.csv")

print("Dataset shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())


if df.empty:
    raise ValueError("Dataset is empty.")


# ============================================================
# FEATURE COLUMNS
# ============================================================

FEATURE_COLUMNS = [
    column
    for column in df.columns
    if column not in TARGET_COLUMNS
    and column not in ["candidate_id", "target_role"]
]


X = df[FEATURE_COLUMNS]


print("\nNumber of features:", len(FEATURE_COLUMNS))
print("\nFeatures:")
print(FEATURE_COLUMNS)


# ============================================================
# TRAIN ONE MODEL FOR EACH ROLE
# ============================================================

results = []


for target in TARGET_COLUMNS:

    print("\n")
    print("=" * 70)
    print(f"TRAINING: {target}")
    print("=" * 70)

    y = df[target]

    # --------------------------------------------------------
    # Train / validation / test split
    # --------------------------------------------------------

    X_train, X_temp, y_train, y_temp = train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=42,
        stratify=y
    )

    X_validation, X_test, y_validation, y_test = train_test_split(
        X_temp,
        y_temp,
        test_size=0.50,
        random_state=42,
        stratify=y_temp
    )

    print("Training rows:", len(X_train))
    print("Validation rows:", len(X_validation))
    print("Test rows:", len(X_test))


    # --------------------------------------------------------
    # Pipeline
    # --------------------------------------------------------

    model = Pipeline(
        steps=[

            (
                "imputer",
                SimpleImputer(
                    strategy="median"
                )
            ),

            (
                "random_forest",
                RandomForestClassifier(

                    # Number of decision trees
                    n_estimators=300,

                    # Maximum tree depth
                    max_depth=12,

                    # Minimum samples required to split a node
                    min_samples_split=5,

                    # Minimum samples allowed in leaf
                    min_samples_leaf=2,

                    # Random subset of features at each split
                    max_features="sqrt",

                    # Useful when classes are imbalanced
                    class_weight="balanced",

                    random_state=42,

                    # Use all CPU cores
                    n_jobs=-1
                )
            )
        ]
    )


    # --------------------------------------------------------
    # TRAIN
    # --------------------------------------------------------

    model.fit(
        X_train,
        y_train
    )


    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    validation_probability = (
        model.predict_proba(
            X_validation
        )[:, 1]
    )

    validation_prediction = (
        validation_probability >= 0.50
    ).astype(int)


    validation_f1 = f1_score(
        y_validation,
        validation_prediction,
        zero_division=0
    )

    print(
        f"Validation F1: {validation_f1:.4f}"
    )


    # --------------------------------------------------------
    # FINAL TEST
    # --------------------------------------------------------

    test_probability = (
        model.predict_proba(
            X_test
        )[:, 1]
    )

    test_prediction = (
        test_probability >= 0.50
    ).astype(int)


    accuracy = accuracy_score(
        y_test,
        test_prediction
    )

    precision = precision_score(
        y_test,
        test_prediction,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        test_prediction,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        test_prediction,
        zero_division=0
    )

    roc_auc = roc_auc_score(
        y_test,
        test_probability
    )


    print("\nFINAL TEST RESULTS")
    print(
        f"Accuracy : {accuracy:.4f}"
    )
    print(
        f"Precision: {precision:.4f}"
    )
    print(
        f"Recall   : {recall:.4f}"
    )
    print(
        f"F1       : {f1:.4f}"
    )
    print(
        f"ROC-AUC  : {roc_auc:.4f}"
    )


    # --------------------------------------------------------
    # SAVE MODEL
    # --------------------------------------------------------

    model_path = (
        MODEL_DIR /
        f"{target}.joblib"
    )


    artifact = {

        "model": model,

        "features": FEATURE_COLUMNS,

        "target": target,

        "version": "1.0.0",

        "metrics": {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "roc_auc": roc_auc
        }
    }


    joblib.dump(
        artifact,
        model_path
    )


    print(
        f"\nSaved model → {model_path}"
    )


    results.append({
        "role": target,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "roc_auc": roc_auc
    })


# ============================================================
# SUMMARY
# ============================================================

results_df = pd.DataFrame(results)

print("\n\n")
print("=" * 70)
print("MODEL SUMMARY")
print("=" * 70)

print(
    results_df.to_string(
        index=False
    )
)


results_df.to_csv(
    MODEL_DIR / "model_metrics.csv",
    index=False
)

print(
    "\nMetrics saved to models/model_metrics.csv"
)