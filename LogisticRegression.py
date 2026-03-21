import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

data = pd.read_csv('dataset_regresion_logistica.csv')

print(data.head())
print(data.info())
print(data.describe())

X = data.drop[['edad','ingreso_mensual','visitas_web_mes','tiempo_sitio_min','compras_previas','descuento_usado']]
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler= StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
logistic_model = LogisticRegression()
logistic_model.fit(X_train_scaled, y_train)

y_pred = logistic_model.predict(X_test)
confusion_matrix(y_test, y_pred)
print(classification_report(y_test, y_pred))

accuracy_score(y_test, y_pred)