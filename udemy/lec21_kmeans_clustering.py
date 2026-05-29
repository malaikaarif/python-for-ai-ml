# ============================================================
# Lecture 21: ML Algorithms - K-Means Clustering
# Groups unlabeled data into K clusters based on similarity
# Example: 2D points → 3 clusters
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# ── STEP 1: CREATE DATASET ───────────────────────────────────
# Unlabeled 2D points — no target column, model finds groups
data = np.array([
    [1,2],[2,1],[3,1],    # group 1 — bottom left
    [5,4],[6,5],          # group 2 — middle
    [7,8],[8,7],[9,8],[10,10]  # group 3 — top right
])

# ── STEP 2: TRAIN THE MODEL ──────────────────────────────────
# K=3: find 3 clusters, random_state for reproducibility
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(data)

# ── STEP 3: RESULTS ──────────────────────────────────────────
# Cluster centers = average position of each cluster
print("Cluster Centers:\n", kmeans.cluster_centers_)
# Labels = which cluster each point belongs to (0, 1, or 2)
print("Labels:\n", kmeans.labels_)