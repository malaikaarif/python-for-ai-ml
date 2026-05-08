# ============================================================
# Lecture 22: Model Evaluation Metrics
# Accuracy, Precision, Recall, F1-Score, Confusion Matrix
# ============================================================

import numpy as np
from sklearn.metrics import (confusion_matrix, accuracy_score,
                             precision_score, recall_score, f1_score)

# ── STEP 1: DEFINE TRUE AND PREDICTED LABELS ─────────────────
# y_true = actual results, y_pred = what model predicted
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# ── STEP 2: CONFUSION MATRIX ─────────────────────────────────
# Shows TP, TN, FP, FN in a 2x2 grid
cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:")
print(cm)

# ── STEP 3: ACCURACY ─────────────────────────────────────────
# Correct predictions / Total predictions
accuracy = accuracy_score(y_true, y_pred)
print("Accuracy:", accuracy)

# ── STEP 4: PRECISION ────────────────────────────────────────
# Out of all predicted positives, how many were actually positive
precision = precision_score(y_true, y_pred)
print("Precision:", precision)

# ── STEP 5: RECALL ───────────────────────────────────────────
# Out of all actual positives, how many did model catch
recall = recall_score(y_true, y_pred)
print("Recall:", recall)

# ── STEP 6: F1 SCORE ─────────────────────────────────────────
# Balance between Precision and Recall
f1 = f1_score(y_true, y_pred)
print("F1 Score:", f1)