from flask import Flask, render_template, request
import LinearRegression

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

@app.route('/linear-regression-app')
def linear_app():
    return render_template('linear_app.html')

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
    return render_template('salary_app.html')

if __name__ == '__main__':
    app.run(debug=True)
