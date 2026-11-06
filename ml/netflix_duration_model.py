"""Train a baseline model to estimate movie duration from catalog metadata."""

import argparse
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def train_duration_model(data_path: str, model_path: str) -> dict:
    data = pd.read_csv(data_path)
    data = data[data["type"].eq("Movie")].copy()
    data = data.dropna(subset=["duration", "release_year"])

    features = ["release_year", "type", "genre", "country"]
    target = "duration"
    x_train, x_test, y_train, y_test = train_test_split(
        data[features], data[target], test_size=0.2, random_state=42
    )

    numeric_features = ["release_year"]
    categorical_features = ["type", "genre", "country"]
    preprocessor = ColumnTransformer(
        transformers=[
            ("numeric", SimpleImputer(strategy="median"), numeric_features),
            (
                "categorical",
                Pipeline(
                    [
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("encoder", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                categorical_features,
            ),
        ]
    )
    model = Pipeline(
        [
            ("preprocessor", preprocessor),
            (
                "regressor",
                RandomForestRegressor(
                    n_estimators=250, random_state=42, n_jobs=-1, min_samples_leaf=2
                ),
            ),
        ]
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    metrics = {
        "rows_used": int(len(data)),
        "mean_absolute_error_minutes": round(float(mean_absolute_error(y_test, predictions)), 2),
        "r2_score": round(float(r2_score(y_test, predictions)), 3),
    }

    output = Path(model_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output)
    return metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", default="netflix_data.csv")
    parser.add_argument("--model", default="artifacts/netflix_duration_model.joblib")
    args = parser.parse_args()
    print(train_duration_model(args.data, args.model))
