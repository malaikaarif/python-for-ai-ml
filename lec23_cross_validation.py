# ============================================================
# Lecture 23: Cross Validation Techniques
# Evaluates model performance more reliably than single split
# ============================================================

from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

# ── STEP 1: GENERATE DATASET ─────────────────────────────────
# Synthetic regression data: 100 samples, 1 feature, some noise
x, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)

# ── STEP 2: SIMPLE TRAIN/TEST SPLIT ──────────────────────────
# Basic evaluation: 80% train, 20% test
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(x_train, y_train)
print("Simple Train/Test R² Score:", model.score(x_test, y_test))

# ── STEP 3: K-FOLD CROSS VALIDATION ──────────────────────────
# Splits data into 5 folds, trains/tests 5 times
# More reliable than single split — reduces bias
kf = KFold(n_splits=5, shuffle=True, random_state=42)
model = LinearRegression()

# cv=kf means use our KFold strategy
# scoring='r2' measures how well model fits (1.0 = perfect)
scores = cross_val_score(model, x, y, cv=kf, scoring='r2')

print("Cross-Validation Scores:", scores)
print("Average Cross-Validation Score:", scores.mean())

print("Done")