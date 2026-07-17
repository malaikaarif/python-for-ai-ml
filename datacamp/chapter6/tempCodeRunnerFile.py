import pandas as pd
model_results = {
    "random_forest": {"accuracy": 0.92, "precision": 0.91,
                      "recall": 0.93, "f1": 0.92},
    "logistic_reg":  {"accuracy": 0.85, "precision": 0.84,
                      "recall": 0.86, "f1": 0.85},
    "svm":           {"accuracy": 0.88, "precision": 0.87,
                      "recall": 0.89, "f1": 0.88},
    "neural_net":    {"accuracy": 0.95, "precision": 0.94,
                      "recall": 0.96, "f1": 0.95}
}

# 1. Print accuracy of random_forest
print(model_results["random_forest"]["accuracy"])
# 2. Print all model names (keys)
print(model_results.keys())
# 3. Which model has highest accuracy?
#    (write code to find it, don't hardcode!)
bestmodel = max(model_results, key=lambda x: model_results [x]["accuracy"])
print(bestmodel)
# 4. Convert to DataFrame
df=pd.DataFrame(model_results)

# 5. Print the DataFrame
print(df)
# 6. Using loc - get all metrics for neural_net
print(df.loc[:,"neural_net"])
# 7. Using iloc - get first 2 models
print(df.iloc[:,0:2])
# 8. Print: "Best model is X with accuracy Y%"

bestaccuarcy = model_results[bestmodel]["accuracy"]
print(f"Best model is {bestmodel} with accuracy {bestaccuarcy*100:.2f}%")
