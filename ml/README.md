# Machine Learning

`netflix_duration_model.py` trains a reproducible baseline regression model
that estimates movie duration from release year, genre, country, and content
type. It demonstrates a complete machine-learning workflow: feature selection,
missing-value imputation, one-hot encoding, train/test splitting, model
training, evaluation, and model serialization.

Run it from the repository root:

```bash
python ml/netflix_duration_model.py
```

The script reports **MAE** (average error in minutes) and **R²**, then writes
the model to `artifacts/netflix_duration_model.joblib`. This is a portfolio
baseline, not a production forecasting system; model performance should be
compared with a simple baseline before business use.
