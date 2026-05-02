import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # important for Flask
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler


def save_confusion_matrix(cm):
    """
    Save confusion matrix as an image
    """
    os.makedirs("static/images", exist_ok=True)

    plt.figure(figsize=(6, 5))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Purples",
        xticklabels=["Not Hospitalized", "Hospitalized"],
        yticklabels=["Not Hospitalized", "Hospitalized"]
    )

    plt.title("Confusion Matrix - Logistic Regression")
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.tight_layout()
    plt.savefig("static/images/confusion_matrix_logistic.png")
    plt.close()


def save_scatter_plot(data):
    """
    Save scatter plot visualization
    """
    os.makedirs("static/images", exist_ok=True)

    plt.figure(figsize=(8, 6))

    not_hospitalized = data[data["hospitalized"] == 0]
    hospitalized = data[data["hospitalized"] == 1]

    plt.scatter(
        not_hospitalized["age"],
        not_hospitalized["shortness_of_breath"],
        alpha=0.7,
        label="Not Hospitalized"
    )

    plt.scatter(
        hospitalized["age"],
        hospitalized["shortness_of_breath"],
        alpha=0.7,
        label="Hospitalized"
    )

    plt.xlabel("Age")
    plt.ylabel("Shortness of Breath")
    plt.title("Logistic Regression Visualization")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("static/images/logistic_scatter_plot.png")
    plt.close()


def save_logistic_curve(original_data):
    """
    Save a cleaner logistic regression curve using a custom risk score
    to better visualize the sigmoid shape.
    """
    os.makedirs("static/images", exist_ok=True)

    # Work only with ages up to 70
    data_curve = original_data[original_data["age"] <= 70].copy()

    # Create a simplified risk score
    data_curve["risk_score"] = (
        data_curve["age"] * 0.05 +
        data_curve["fever"] * 1.5 +
        data_curve["cough"] * 1.0 +
        data_curve["fatigue"] * 1.0 +
        data_curve["shortness_of_breath"] * 2.0 +
        data_curve["diabetes"] * 1.2 +
        data_curve["hypertension"] * 1.2 +
        data_curve["heart_disease"] * 1.5 +
        data_curve["asthma"] * 1.0 +
        data_curve["cancer"] * 1.5
    )

    X_curve = data_curve[["risk_score"]]
    y_curve = data_curve["hospitalized"]

    # Train simple logistic regression for visualization
    curve_model = LogisticRegression()
    curve_model.fit(X_curve, y_curve)

    # Smooth curve
    x_min = X_curve["risk_score"].min()
    x_max = X_curve["risk_score"].max()
    score_range = np.linspace(x_min, x_max, 500).reshape(-1, 1)
    probability_curve = curve_model.predict_proba(score_range)[:, 1]

    # Separate classes
    class_0 = data_curve[data_curve["hospitalized"] == 0]
    class_1 = data_curve[data_curve["hospitalized"] == 1]

    # Create figure
    plt.figure(figsize=(9, 5))

    # Class 0 points (bottom)
    plt.scatter(
        class_0["risk_score"],
        np.zeros(len(class_0)),
        color="red",
        alpha=0.35,
        s=12,
        label="Not Hospitalized (0)"
    )

    # Class 1 points (top)
    plt.scatter(
        class_1["risk_score"],
        np.ones(len(class_1)),
        color="cyan",
        alpha=0.5,
        s=12,
        label="Hospitalized (1)"
    )

    # Logistic curve
    plt.plot(
        score_range,
        probability_curve,
        color="black",
        linewidth=2.5,
        label="Logistic Curve"
    )

    plt.title("Logistic Regression", fontsize=13)
    plt.xlabel("Risk Score")
    plt.ylabel("Predicted Probability")
    plt.ylim(-0.05, 1.05)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    # Save image
    plt.savefig("static/images/logistic_curve.png", dpi=300, bbox_inches="tight")
    plt.close()


def train_model():
    # =========================
    # 1. Load data
    # =========================
    original_data = pd.read_csv("data/covid_symptoms_severity_prediction.csv")

    # Save extra visualizations
    save_scatter_plot(original_data)
    save_logistic_curve(original_data)

    # =========================
    # 2. Convert categorical variables to numeric
    # =========================
    data = pd.get_dummies(original_data, drop_first=True)

    # =========================
    # 3. Split data
    # =========================
    X = data.drop("hospitalized", axis=1)
    y = data["hospitalized"]

    # Save column names for later use
    feature_names = X.columns

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # =========================
    # 4. Scale data
    # =========================
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # =========================
    # 5. Train model
    # =========================
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # =========================
    # 6. Predict
    # =========================
    y_pred = model.predict(X_test)

    # =========================
    # 7. Metrics
    # =========================
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    print("Accuracy:", accuracy)
    print("Confusion Matrix:\n", cm)
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # =========================
    # 8. Save confusion matrix image
    # =========================
    save_confusion_matrix(cm)

    return model, scaler, feature_names, accuracy, cm, report


# =========================================
# Train once when file is loaded
# =========================================
_model, _scaler, _feature_names, _accuracy, _cm, _report = train_model()


def get_prediction(input_data: dict):
    """
    Predict hospitalization probability for one patient
    """
    df = pd.DataFrame([input_data])

    # Apply same encoding
    df = pd.get_dummies(df)

    # Align columns with training data
    df = df.reindex(columns=_feature_names, fill_value=0)

    # Scale
    df_scaled = _scaler.transform(df)

    # Predict
    prediction = _model.predict(df_scaled)
    probability = _model.predict_proba(df_scaled)

    return {
        "prediction": int(prediction[0]),
        "probability": float(probability[0][1])  # Probability of hospitalization
    }


def handle_form(form):
    """
    Receive data from Flask form and return prediction
    """
    input_data = {
        "age": float(form['age']),
        "gender": form['gender'],
        "vaccination_status": form['vaccination_status'],
        "fever": float(form['fever']),
        "cough": float(form['cough']),
        "fatigue": float(form['fatigue']),
        "shortness_of_breath": float(form['shortness_of_breath']),
        "loss_of_smell": float(form['loss_of_smell']),
        "headache": float(form['headache']),
        "diabetes": float(form['diabetes']),
        "hypertension": float(form['hypertension']),
        "heart_disease": float(form['heart_disease']),
        "asthma": float(form['asthma']),
        "cancer": float(form['cancer'])
    }

    return get_prediction(input_data)


def get_model_metrics():
    """
    Return model evaluation metrics for Flask
    """
    return {
        "accuracy": _accuracy,
        "confusion_matrix": _cm.tolist(),
        "classification_report": _report
    }