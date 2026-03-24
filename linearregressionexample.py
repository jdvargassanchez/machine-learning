from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Cargar dataset
data = pd.read_csv('data.csv')

X = data[['hours']]
y = data['score']

# Entrenar modelo
model = LinearRegression()
model.fit(X, y)

@app.route('/linear-regression-app', methods=['GET', 'POST'])
def linear_app():
    prediction = None

    if request.method == 'POST':
        hours = float(request.form['hours'])
        prediction = model.predict([[hours]])[0]

    return render_template('linear_app.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)