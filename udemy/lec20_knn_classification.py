# ============================================================
# Lecture 20: ML Algorithms - K-Nearest Neighbors (KNN)
# Classifies a data point based on its K closest neighbors
# Example: Weight + Color Score → Apple or Orange
# ============================================================

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# ── STEP 1: CREATE DATASET ───────────────────────────────────
# Labeled data: fruit features mapped to fruit type
# 1 = Apple, 0 = Orange
data = pd.DataFrame({
    "Weight":      [150, 170, 160, 180, 120, 130, 140, 150],
    "Color_Score": [7, 8, 8, 9, 6, 7, 7, 8],
    "Fruit":       [1, 1, 1, 1, 0, 0, 0, 0]
})

# ── STEP 2: DEFINE FEATURES AND TARGET ──────────────────────
x = data[["Weight", "Color_Score"]]  # 2 features (2D) → input
y = data["Fruit"]                    # target → 0 or 1

# ── STEP 3: TRAIN THE MODEL ──────────────────────────────────
# K=3 means: look at 3 nearest neighbors and take majority vote
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x, y)

# ── STEP 4: PREDICT ON NEW DATA ──────────────────────────────
# Predict fruit type for weight=155g, color_score=7.5
new_data = [[155, 7.5]]
prediction = knn.predict(new_data)

print(f"The predicted fruit is: {'Apple' if prediction[0] == 1 else 'Orange'}")