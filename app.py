from flask import Flask, render_template, request
import LinearRegression
import LogisticRegressionModel

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Flask"

@app.route('/FirstPage')
def firstPage():
    return render_template('index.html')

@app.route('/LineaRegression', methods=["GET", "POST"])
def calculateGrade():
    calculateResult = None
    if request.method == "POST":
        hours = float(request.form["hours"])
        calculateResult = LinearRegression.calculateGrade(hours)
    return render_template("linearRegressionGrades.html", result = calculateResult)
    
