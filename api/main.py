from fastapi import FastAPI
import os
import joblib
import pandas as pd

app = FastAPI()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_DIR = os.path.join(BASE_DIR, "model")

model = joblib.load(
    os.path.join(MODEL_DIR, "churn_model.pkl")
)

feature_columns = joblib.load(
    os.path.join(MODEL_DIR, "feature_columns.pkl")
)

scaler = joblib.load(
    os.path.join(MODEL_DIR, "scaler.pkl")
)


@app.get("/")
def home():
    return {"message": "Customer Churn API is running"}


@app.post("/predict")
def predict(customer_data: dict):

    df = pd.DataFrame([customer_data])

    df_encoded = pd.get_dummies(
        df,
        drop_first=True
    )

    df_encoded = df_encoded.reindex(
        columns=feature_columns,
        fill_value=0
    )

    df_scaled = scaler.transform(df_encoded)

    prediction = model.predict(df_scaled)[0]

    probability = model.predict_proba(df_scaled)[0][1]

    return {
        "churn_prediction": "Yes" if prediction == 1 else "No",
        "churn_probability": round(float(probability), 4),
        "churn_probability_percent": round(float(probability * 100), 2)
    }