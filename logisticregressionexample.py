import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler


def train_model():
    # load data
    data = pd.read_csv("data/covid_symptoms_severity_prediction.csv")

    # split data
    X = data.drop("hospitalized", axis=1)
    y = data["hospitalized"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # scale data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # evaluate
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:", confusion_matrix(y_test, y_pred))
    print("Classification Report:", classification_report(y_test, y_pred))

    return model, scaler


# Train once when the module is imported
_model, _scaler = train_model()


def g et_prediction(age, gender, vaccination_status, fever, cough, fatigue,
                   shortness_of_breath, loss_of_smell, headache, diabetes,
                   hypertension, heart_disease, asthma, cancer):
    features = np.array([[age, gender, vaccination_status, fever, cough, fatigue,
                           shortness_of_breath, loss_of_smell, headache, diabetes,
                           hypertension, heart_disease, asthma, cancer]])
    features_scaled = _scaler.transform(features)
    prediction = _model.predict(features_scaled)
    return float(prediction[0])


#handle form   
def handle_form(form):
    age = float(form['age'])
    gender = float(form['gender'])
    vaccination_status = float(form['vaccination_status'])
    fever = float(form['fever'])
    cough = float(form['cough'])
    fatigue = float(form['fatigue'])
    shortness_of_breath = float(form['shortness_of_breath'])
    loss_of_smell = float(form['loss_of_smell'])
    headache = float(form['headache'])
    diabetes = float(form['diabetes'])
    hypertension = float(form['hypertension'])
    heart_disease = float(form['heart_disease'])
    asthma = float(form['asthma'])
    cancer = float(form['cancer'])
    return get_prediction(
        age, gender, vaccination_status, fever, cough, fatigue,
        shortness_of_breath, loss_of_smell, headache, diabetes,
        hypertension, heart_disease, asthma, cancer
    )