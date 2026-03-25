# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# ── 1. Load data ─────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(__file__)
data = pd.read_csv(os.path.join(BASE_DIR, "data", "train.csv"))

X = data[["experience"]]   # independent variable
y = data["salary_usd"]     # dependent variable

# ── 2. Split data into training and testing sets ──────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ── 3. Train model ───────────────────────────────────────────────────────────
model = LinearRegression()
model.fit(X_train, y_train)

# ── 4. Predict ───────────────────────────────────────────────────────────────
y_pred = model.predict(X_test)

# ── 5. Model metrics ─────────────────────────────────────────────────────────
mae  = mean_absolute_error(y_test, y_pred)
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)

print("=" * 52)
print("   SIMPLE LINEAR REGRESSION -- Salary Predictor")
print("=" * 52)
print("  Independent variable (X) : experience")
print("  Dependent variable   (y) : salary_usd")
print("-" * 52)
print(f"  Intercept  (b0)          : ${model.intercept_:,.2f}")
print(f"  Coefficient (b1)         : ${model.coef_[0]:,.2f} / year of exp.")
print(f"  Equation   : y_hat = {model.intercept_:,.2f} + {model.coef_[0]:,.2f} * X")
print("=" * 52)
print("  EVALUATION METRICS  (test set - 20 %)")
print("-" * 52)
print(f"  R2   (coefficient of determination) : {r2:.4f}")
print(f"  MAE  (mean absolute error)          : ${mae:,.2f}")
print(f"  RMSE (root mean squared error)      : ${rmse:,.2f}")
print("=" * 52)

# ── 6. Comparison table: actual vs predicted ──────────────────────────────────
results = X_test.copy()
results["salary_actual"]    = y_test.values
results["salary_predicted"] = y_pred.round(2)
results["error"]            = (results["salary_predicted"] - results["salary_actual"]).round(2)
results = results.reset_index(drop=True)

print("\n  TABLE: Actual vs Predicted (first 15 rows)")
print("-" * 52)
print(results.head(15).to_string(index=True))
print("=" * 52)

# ── 7. Scatter plot with regression line ─────────────────────────────────────
sns.set_theme(style="darkgrid")
fig, ax = plt.subplots(figsize=(9, 6))

# Random sample to avoid overplotting
sample = data.sample(n=1000, random_state=42)
ax.scatter(
    sample["experience"], sample["salary_usd"],
    color="#a78bfa", alpha=0.45, edgecolors="none", s=30,
    label="Actual data (sample)"
)

# Regression line
x_line = np.linspace(X["experience"].min(), X["experience"].max(), 200)
y_line = model.predict(x_line.reshape(-1, 1))
ax.plot(x_line, y_line, color="#f59e0b", linewidth=2.5, label="Regression line")

ax.set_title("Simple Linear Regression\nYears of Experience vs Salary (USD)", fontsize=14, fontweight="bold")
ax.set_xlabel("Years of experience (X)", fontsize=12)
ax.set_ylabel("Annual salary in USD (y)", fontsize=12)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"${v:,.0f}"))
ax.legend(fontsize=10)

# Equation annotation
eq_text = f"y_hat = {model.intercept_:,.0f} + {model.coef_[0]:,.0f} * X\n R2 = {r2:.4f}"
ax.text(0.04, 0.92, eq_text, transform=ax.transAxes,
        fontsize=10, color="white",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#1e1b4b", alpha=0.7))

plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, "data", "regression_salary.png"), dpi=150)
plt.show()
print("\n  Chart saved to: data/regression_salary.png")
