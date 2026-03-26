# Machine Learning App

An educational web application built with **Flask** that allows users to explore Machine Learning concepts, real-world use cases, and interact with predictive models trained with `scikit-learn`.

---

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Application Routes](#application-routes)
- [Machine Learning Models](#machine-learning-models)
- [Dataset](#dataset)
- [Team](#team)
- [Dependencies](#dependencies)

---

## Description

This project is an interactive web application focused on Machine Learning education. It includes:

- Theoretical explanations of Linear Regression concepts.
- Real-world ML use cases across different industries.
- Interactive applications where users can enter data and get real-time predictions from trained models.

---

## Project Structure

```
machine-learning/
│
├── app.py                           # Main Flask server
├── LinearRegression.py              # Model: Grade Predictor
├── linearregressionexample.py       # Model: Salary Predictor
├── tabulador.py                     # Auxiliary script
├── requirements.txt                 # Project dependencies
│
├── data/
│   ├── train.csv                    # Salary dataset (training source)
│   └── data_dictionary.csv          # Dataset variable dictionary
│
├── templates/
│   ├── index.html                   # Home page / navigation menu
│   ├── linear_concepts.html         # Linear Regression concepts
│   ├── linearRegressionGrades.html  # App: Grade Predictor
│   ├── salary_app.html              # App: Salary Predictor
│   ├── use_cases1.html              # Use Case 1: House Price Prediction
│   ├── use_cases2.html              # Use Case 2: Anti-Procrastination App
│   ├── use_cases3.html              # Use Case 3: Smart Health Colombia
│   └── use_cases4.html              # Use Case 4: Customer Churn Prediction
│
└── static/
    ├── css/                         # Custom stylesheets
    ├── js/                          # Navigation scripts
    └── images/                      # Team member photos
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/jdvargassanchez/machine-learning.git
cd machine-learning
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run the Flask development server:

```bash
python app.py
```

Then open your browser at: [http://localhost:5000](http://localhost:5000)

---

## Application Routes

| Route | Description |
|-------|-------------|
| `/` | Home page with navigation menu |
| `/linear-regression-concepts` | Theoretical concepts of Linear Regression |
| `/linear-regression-app` | Grade Predictor application |
| `/salary-predictor` | Salary Predictor application |
| `/use-case1` | Use Case 1 — House Price Prediction |
| `/use-case2` | Use Case 2 — Anti-Procrastination App |
| `/use-case3` | Use Case 3 — Smart Health Colombia |
| `/use-case4` | Use Case 4 — Customer Churn Prediction |

---

## Machine Learning Models

### Grade Predictor (`LinearRegression.py`)

Uses **Linear Regression** to predict a student's final grade.

- **Input variable (X):** Study hours (`Study Hours`)
- **Output variable (y):** Final grade (`Final Grade`, scale 1.0 – 5.0)
- **Data:** Synthetic dataset of 20 records defined directly in the code.

### Salary Predictor (`linearregressionexample.py`)

Uses **Linear Regression** to predict a developer's salary.

- **Input variable (X):** Years of professional experience (`experience`)
- **Output variable (y):** Salary in US dollars (`salary_usd`)
- **Data:** `data/train.csv` file

---

## Dataset

The `data/train.csv` file contains information about software developers and their salaries. Below is a description of its columns:

| Column | Type | Description |
|--------|------|-------------|
| `experience` | number | Years of professional coding experience |
| `country` | string | Country of residence |
| `education` | string | Highest level of formal education |
| `languages` | string | Primary programming languages |
| `frameworks` | string | Primary frameworks used |
| `company_size` | string | Number of employees in the company |
| `salary_usd` | target | **Target variable:** Salary in USD (to predict) |

---

## Team

| Name |
|------|
| Juan David Vargas |
| Camilo Andrés Sichaca |
| Sharick Lorena Doncel |
| Santiago José Morales |

---

## Dependencies

```
flask
pandas
matplotlib
scikit-learn
```

> Install with: `pip install -r requirements.txt`
