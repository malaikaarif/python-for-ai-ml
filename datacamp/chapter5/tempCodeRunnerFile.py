

# Q10. Complete analysis plot:
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
x = np.linspace(0, 10, 100)
y_true = 2 * x + 1
y_pred = y_true + np.random.normal(0, 2, 100)

# Create figure with 2 subplots side by side:
# Left plot: scatter of y_true vs y_pred
#            add diagonal line (perfect predictions line)
#            title: "Predictions vs Actual"

# Right plot: histogram of errors (y_pred - y_true)
#             title: "Error Distribution"
# hint: fig, axes = plt.subplots(1, 2, figsize=(12, 5))
#       axes[0].scatter(...)
#       axes[1].hist(...)
# 5. plt.tight_layout()
# 6. plt.show()



fig,axes = plt.subplots(1,2,figsize=(12,5))
axes[0].scatter(y_true,y_pred)
axes[0].plot([y_true.min(),y_true.max()],[y_true.min(),y_true.max()],color="red", linestyle="--", label="Perfect prediction")

axes[0].set_xlabel("Actual")
axes[0].set_ylabel("Predicted")
axes[0].set_title("Predictions vs Actual")
axes[0].legend()
axes[0].grid(True)



errors = y_pred - y_true
axes[1].hist(errors,bins=20,color="orange", alpha=0.7)
axes[1].set_title("Error Distribution")
axes[1].set_xlabel("Error")
axes[1].set_ylabel("Frequency")

plt.tight_layout()
plt.show()

