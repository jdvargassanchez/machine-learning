import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler


def train_model():
    # Load data
    data = pd.read_csv("data/covid_symptoms_severity_prediction.csv")

    # Convert categorical variables to numeric
    data = pd.get_dummies(data, drop_first=True)

    # Split data
    X = data.drop("hospitalized", axis=1)
    y = data["hospitalized"]

    # Save column names for later use
    feature_names = X.columns

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Scale data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    return model, scaler, feature_names


# Train once
_model, _scaler, _feature_names = train_model()


def get_prediction(input_data: dict):
    # Convert input dict to DataFrame
    df = pd.DataFrame([input_data])

    # Apply same encoding
    df = pd.get_dummies(df)

    #  Align columns with training data
    df = df.reindex(columns=_feature_names, fill_value=0)

    # Scale
    df_scaled = _scaler.transform(df)

    # Predict
    prediction = _model.predict(df_scaled)
    probability = _model.predict_proba(df_scaled)

    return {
        "prediction": int(prediction[0]),
        "probability": float(probability[0][1])  # probabilidad de hospitalización
    }


# Handle form (Flask)
def handle_form(form):
    input_data = {
        "age": float(form['age']),
        "gender":form['gender'],
        "vaccination_status":form['vaccination_status'],
        "fever":float(form['fever']),
        "cough":float(form['cough']),
        "fatigue":float(form['fatigue']),
        "shortness_of_breath":float(form['shortness_of_breath']),
        "loss_of_smell":float(form['loss_of_smell']),
        "headache":float(form['headache']),
        "diabetes":float(form['diabetes']),
        "hypertension":float(form['hypertension']),
        "heart_disease":float(form['heart_disease']),
        "asthma":float(form['asthma']),
        "cancer":float(form['cancer'])  
    }

    return get_prediction(input_data)