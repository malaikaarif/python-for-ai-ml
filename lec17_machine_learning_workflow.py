# ============================================================
# Lecture 17: Machine Learning Workflow
# Step-by-step: Load Data → Train Model → Predict
# ============================================================

import pandas as pd
from sklearn.linear_model import LinearRegression

# ── STEP 1: LOAD / CREATE DATA ───────────────────────────────
# Real-world data: house size (sq ft) vs price ($)
data = pd.DataFrame({
    "Size":  [500, 1000, 1500, 2000, 2500],   # input feature
    "Price": [150000, 300000, 450000, 600000, 750000]  # target label
})

print("DataFrame:")
print(data)

# ── STEP 2: SPLIT FEATURES AND TARGET ───────────────────────
x = data[["Size"]]   # feature matrix (2D) → input to model
y = data["Price"]    # target vector (1D) → what we want to predict

# ── STEP 3: TRAIN THE MODEL ──────────────────────────────────
# LinearRegression finds the best line through the data
model = LinearRegression()
model.fit(x, y)      # model learns the pattern: Price = m*Size + b

print("Model Training Complete!")

# ── STEP 4: MAKE A PREDICTION ────────────────────────────────
# Predict price for a house that is 3000 sq ft (unseen data)
predicted_price = model.predict([[3000]])
print(f"Predicted Price for 3000 sq ft house: ${predicted_price[0]:.2f}")