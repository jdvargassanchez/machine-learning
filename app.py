from flask import Flask, render_template, request
import LinearRegression

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/linear-regression', methods=["GET", "POST"])
def calculateGrade():
    calculateResult = None
    if request.method == "POST":
        hours = float(request.form["hours"])
        calculateResult = LinearRegression.calculateGrade(hours)
    return render_template("linearRegressionGrades.html", result = calculateResult)

@app.route('/use-case1')
def use_case1():
    return render_template('use_cases1.html')