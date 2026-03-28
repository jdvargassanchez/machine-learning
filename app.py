from flask import Flask, render_template, request
import LinearRegression
import linearregressionexample
import logisticregressionexample

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/use-case1')
def use_case1():
    return render_template('use_cases1.html')
    
@app.route('/linear-regression-concepts')
def linear_concepts():
    return render_template('linear_concepts.html')

@app.route('/logistic-regression-concepts')
def logistic_concepts():
    return render_template('logistic_concepts.html')

@app.route('/linear-regression-app', methods=['GET', 'POST'])
def linear_app():
    result = None
    if request.method == 'POST':
        hours = float(request.form['hours'])
        raw = LinearRegression.calculateGrade(hours)
        result = round(float(raw), 2)
    return render_template('linearRegressionGrades.html', result=result)

@app.route('/use-case2')
def use_case2():
    return render_template('use_cases2.html')

@app.route('/use-case3')
def use_case3():  
    return render_template('use_cases3.html')

@app.route('/use-case4')
def use_case4():
    return render_template('use_cases4.html')

@app.route('/salary-predictor', methods=['GET', 'POST'])
def salary_app():
    prediction = None
    if request.method == 'POST':
        experience = float(request.form['experience'])
        raw = linearregressionexample.get_prediction(experience)
        prediction = round(float(raw), 2)
    return render_template('salary_app.html', prediction=prediction)

@app.route('/logistic-regression-app', methods=['GET', 'POST'])
def logistic_app():
    prediction = None
    if request.method == 'POST':
        age = float(request.form['age'])
        gender = float(request.form['gender'])
        vaccination_status = float(request.form['vaccination_status'])
        fever = float(request.form['fever'])
        cough = float(request.form['cough'])
        fatigue = float(request.form['fatigue'])
        shortness_of_breath = float(request.form['shortness_of_breath'])
        loss_of_smell = float(request.form['loss_of_smell'])
        headache = float(request.form['headache'])
        diabetes = float(request.form['diabetes'])
        hypertension = float(request.form['hypertension'])
        heart_disease = float(request.form['heart_disease'])
        asthma = float(request.form['asthma'])
        cancer = float(request.form['cancer'])
        prediction = logisticregressionexample.get_prediction(
            age, gender, vaccination_status, fever, cough, fatigue,
            shortness_of_breath, loss_of_smell, headache, diabetes,
            hypertension, heart_disease, asthma, cancer
        )
    return render_template('logistic_regression_app.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
