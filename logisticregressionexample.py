import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
import seaborn as sns


#load data
data=pd.read_csv("data/covid_symptoms_severity_prediction.csv")

#explore data
print(data.head())
print(data.info())
print(data.describe())

#split data
X=data.drop("hospitalized", axis=1)
y=data["hospitalized"]

X_train, X_test, y_train, y_test=train_test_split(X,y, test_size=0.2, random_state=42)

#scale data
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

#train model
model=LogisticRegression()
model.fit(X_train, y_train)

#predict
y_pred=model.predict(X_test)

#evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:", confusion_matrix(y_test, y_pred))
print("Classification Report:", classification_report(y_test, y_pred))

#plot
plt.figure(figsize=(8,6))
plt.scatter(X_test[:,0], X_test[:,1], c=y_pred, cmap='viridis')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Logistic Regression")
plt.show()
