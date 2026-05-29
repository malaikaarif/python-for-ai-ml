# ============================================================
# Lecture 16: Types of Machine Learning
# Supervised | Unsupervised | Reinforcement
# ============================================================


# ── 1. SUPERVISED LEARNING (Regression) ─────────────────────
# The model learns from labeled data (input → known output)
# Example: Predict exam score based on hours studied

from sklearn.linear_model import LinearRegression

x = [[0],[1],[2],[3],[4],[5]]  # hours studied
y = [50, 55, 60, 65, 70, 75]  # corresponding scores

model = LinearRegression()
model.fit(x, y)  # train the model

predicted_score = model.predict([[6]])  # predict for 6 hours
print(f"Predicted score for 6 hours of study: {predicted_score[0]:.2f}")







# ── 2. UNSUPERVISED LEARNING (Clustering) ───────────────────
# The model finds hidden patterns in unlabeled data
# Example: Group similar data points into clusters

from sklearn.cluster import KMeans
import numpy as np

data = np.array([[1,1],[1,2],[2,2],[8,8],[8,9],[9,9]])  # 2 natural groups
kmeans = KMeans(n_clusters=2)  # tell model: find 2 clusters
kmeans.fit(data)
print("Cluster assignments:\n", kmeans.labels_)  # 0 or 1 per point






# ── 3. REINFORCEMENT LEARNING (Reward-based) ────────────────
# Agent learns by taking actions and receiving rewards/penalties
# Example: Choose the action with the highest reward

actions = ['Move Left', 'Move Right', 'Stay']

rewards = {
    'Move Left': -1,   # penalty
    'Move Right': +1,  # reward
    'Stay': 0          # neutral
}

# Pick the action that gives maximum reward
best_action = max(rewards, key=rewards.get)
print(f"Best action: {best_action} with reward {rewards[best_action]}")