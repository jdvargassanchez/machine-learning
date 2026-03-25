import pandas as pd
from sklearn.linear_model import LinearRegression

# Cargar datos
import os
data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'train.csv'))

X = data[['experience']]
y = data['salary_usd']

model = LinearRegression()
model.fit(X, y)

#  FUNCIÓN DE PREDICCIÓN
def get_prediction(experience):
    return model.predict([[experience]])[0]