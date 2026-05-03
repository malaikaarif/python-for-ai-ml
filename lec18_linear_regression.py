# ============================================================
# Lecture 18: ML Algorithms - Linear Regression
# Predicts a continuous value based on input features
# Example: Years of Experience → Salary
# ============================================================

import pandas as pd
from sklearn.linear_model import LinearRegression

# ── STEP 1: CREATE DATASET ───────────────────────────────────
# Labeled data: experience (years) mapped to salary ($)
data = pd.DataFrame({
    'Experience': [1, 2, 3, 4, 5],
    'Salary':     [30000, 35000, 40000, 45000, 50000]
})

print("Dataset:")
print(data)

# ── STEP 2: DEFINE FEATURES AND TARGET ──────────────────────
x = data[['Experience']]  # feature (2D) → input
y = data['Salary']        # target (1D) → what we predict

# ── STEP 3: TRAIN THE MODEL ──────────────────────────────────
# Model learns: Salary = m * Experience + b
model = LinearRegression()
model.fit(x, y)

# ── STEP 4: PREDICT ──────────────────────────────────────────
# Predict salary for 6 years of experience (unseen data)
years_of_experience = [[6]]  # must be 2D for predict()
predicted_salary = model.predict(years_of_experience)

print(f"Predicted salary for {years_of_experience[0][0]} years of experience: ${predicted_salary[0]:.2f}")