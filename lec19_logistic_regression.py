# ============================================================
# Lecture 19: ML Algorithms - Logistic Regression
# Predicts a binary outcome (Pass/Fail, Yes/No, 0/1)
# Example: Hours Studied → Pass or Fail
# ============================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ── STEP 1: CREATE DATASET ───────────────────────────────────
# Labeled data: hours studied mapped to result (0=Fail, 1=Pass)
data = pd.DataFrame({
    "Hours_studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Result":        [0, 0, 0, 1, 1, 0, 0, 0, 1, 1]
})

print("Dataset:")
print(data)

# ── STEP 2: DEFINE FEATURES AND TARGET ──────────────────────
x = data[["Hours_studied"]]  # feature (2D) → input
y = data["Result"]           # target (1D) → 0 or 1

# ── STEP 3: SPLIT DATA ───────────────────────────────────────
# 80% for training, 20% for testing
# always unpack 4 values from train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# ── STEP 4: TRAIN THE MODEL ──────────────────────────────────
# Logistic Regression learns the probability of passing
model = LogisticRegression()
model.fit(x_train, y_train)

# ── STEP 5: EVALUATE THE MODEL ───────────────────────────────
# Compare predicted values vs actual test labels
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# ── STEP 6: PREDICT ON NEW DATA ──────────────────────────────
# Predict whether a student studying 6.5 hours will pass or fail
new_data = [[6.5]]
prediction = model.predict(new_data)
print(f"Predicted Result for 6.5 hours of study: {'Pass' if prediction[0] == 1 else 'Fail'}")