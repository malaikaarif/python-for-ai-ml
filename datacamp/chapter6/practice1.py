# ============================================
# Intermediate Python - Chapter 2
# Dictionaries & Pandas - PRACTICE
# ============================================

import pandas as pd
import numpy as np

# ===== LEVEL 1: DICTIONARY BASICS =====

# Q1. Predict the output WITHOUT running:
person = {"name": "Malaika", "age": 22, "city": "Okara"}

print(person["name"])             # Malaika
print(person["age"] + 8)          # 30
print("city" in person)           # True
print("salary" in person)         # False
print(len(person))                # 3









# Q2. Fix the bugs:
student = {"name": "Ali", "grade": "A"}

# Bug 1:
print(student[name])          # bug!       print(student["name"])

# Bug 2:
student["age"] == 20          # bug! (want to ADD age)        student["age"]=20

# Bug 3:
del student                   # bug! (want to delete only "grade")    del student["grade"]

# Bug 4:
print(student.key())          # bug!                         .keys()









# ===== LEVEL 2: DICTIONARY MANIPULATION =====

# Q3. Start with this dictionary and do all operations:
scores = {"math": 85, "english": 90, "science": 78}

# 1. Add "history": 88
scores["history"] = 88
# 2. Update "math" to 95
scores["math"] = 95
# 3. Delete "english"
del scores ["english"]
# 4. Check if "science" exists
print("science" in scores)
# 5. Print all keys
print(scores.keys())
# 6. Print all values
print(scores.values())
# 7. Print final dictionary
print(scores)










# Q4. Nested dictionary challenge:
ml_project = {
    "model": {
        "name": "RandomForest",
        "layers": 3,
        "accuracy": 0.92
    },
    "data": {
        "samples": 1000,
        "features": 15,
        "target": "price"
    },
    "training": {
        "epochs": 100,
        "learning_rate": 0.001,
        "batch_size": 32
    }
}

# Access:
# 1. Model name
print(ml_project["model"]["name"])
# 2. Number of features
print(ml_project["data"]["features"])
# 3. Learning rate
print(ml_project["training"]["learning_rate"])
# 4. Add "optimizer": "adam" to training
ml_project["training"]["optimizer"] = "adam"
# 5. Update accuracy to 0.95
ml_project["model"]["accuracy"] = 0.95
# 6. Print entire training config
print(ml_project["training"])










# ===== LEVEL 3: PANDAS BASICS =====

# Q5. Create a DataFrame from this dictionary:
import pandas as pd
data = {
    "name": ["Alice", "Bob", "Sara", "John", "Emma"],
    "age": [25, 30, 22, 28, 35],
    "salary": [50000, 60000, 45000, 55000, 70000],
    "city": ["NYC", "LA", "NYC", "Chicago", "LA"],
    "experience": [2, 5, 1, 4, 8]
}

# 1. Create DataFrame
df = pd.DataFrame(data)
print(df)
# 2. Print first 3 rows
print(df.head(3))
# 3. Print last 2 rows
print(df.tail(2))
# 4. Print shape
print(df.shape)
# 5. Print dtypes
print(df.dtypes)
# 6. Print info()
print(df.info())
# 7. Print describe()
print(df.describe())






# These are METHODS - need brackets!
df.head()      # ✅
df.tail()      # ✅
df.info()      # ✅
df.describe()  # ✅

# These are ATTRIBUTES - no brackets!
df.shape       # ✅ (no brackets!)
df.dtypes      # ✅ (no brackets!)
df.index       # ✅ (no brackets!)
df.columns     # ✅ (no brackets!)












# Q6. Predict the output:
import pandas as pd
df = pd.DataFrame({
    "x": [1, 2, 3],
    "y": [4, 5, 6],
    "z": [7, 8, 9]
})

print(type(df["x"]))       # Series or DataFrame?          series
print(type(df[["x"]]))     # Series or DataFrame?          dataframe
print(type(df[["x","y"]])) # Series or DataFrame?          dataframe
print(df["x"][0])          # what value?                   1
print(df[0:2])             # what prints?                  after in dataframe then predict





# df[0:2] gives first 2 ROWS (not just x column!)
# ALL columns, rows 0 and 1:
#    x  y  z
# 0  1  4  7
# 1  2  5  8



# df[0:2] gives ALL columns, first 2 rows!

# Square brackets with slice → ROWS
df[0:2]        # → first 2 rows, ALL columns

# Square brackets with string → COLUMN
df["x"]        # → x column, ALL rows

# Don't mix these up!











# ===== LEVEL 4: loc AND iloc =====

# Q7. Given this DataFrame:
import pandas as pd
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Sara", "John"],
    "age": [25, 30, 22, 28],
    "salary": [50000, 60000, 45000, 55000]
})
df.index = ["alice", "bob", "sara", "john"]

# Using LOC - predict output:
print(df.loc["alice"])                            # complete row of alice
print(df.loc["alice", "name"])                    # Alice
print(df.loc["alice":"bob"])      # how many rows?         2
print(df.loc[:, "name"])                                   # all rows but name column (all names)
print(df.loc["alice":"sara", "name":"age"])                # name and age of alice,bob and sara

# Using ILOC - predict output:
print(df.iloc[0])                # row of alice
print(df.iloc[0, 0])             # Alice
print(df.iloc[0:2])               # how many rows?      2
print(df.iloc[:, 0])               # all rows but name column (all names)
print(df.iloc[0:2, 0:2])           # name and age of alice,bob










# Q8. loc vs iloc trap:
import pandas as pd
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Sara"],
    "age": [25, 30, 22]
})

# Both should give same result but different syntax:
# Using loc:
result1 = df.loc[0:1, "name":"age"]        
# Using iloc:
result2 = df.iloc[0:1, 0:2]

# Q: Do result1 and result2 give same number of rows?
# Explain why or why not as a comment!





# They give same columns but different number of rows

# result1 = df.loc[0:1, "name":"age"]
# loc is INCLUSIVE → rows 0 AND 1
# → 2 rows (Alice AND Bob)!

# result2 = df.iloc[0:1, 0:2]
# iloc is EXCLUSIVE → row 0 only
# → 1 row (Alice only)!





# result1 (loc - 2 rows):    result2 (iloc - 1 row):
#    name  age                  name  age
# 0  Alice   25              0  Alice   25
# 1    Bob   30



# loc end is INCLUSIVE  → [0:1] gives rows 0,1
# iloc end is EXCLUSIVE → [0:1] gives row 0 only
#                         [0:2] gives rows 0,1

# This is the most common trap in Pandas interviews! 💡















# ===== LEVEL 5: AI/ML CHALLENGE =====

# Q9. Dataset exploration (first thing in every ML project!):
# Create this dataset:
import pandas as pd
ml_data = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "study_hours": [2, 5, 1, 8, 3, 7, 4, 6, 2, 9],
    "sleep_hours": [8, 6, 9, 5, 7, 6, 7, 5, 8, 4],
    "score": [55, 78, 45, 92, 63, 88, 70, 85, 52, 95],
    "passed": [False, True, False, True, True,
               True, True, True, False, True]
})

# Explore the dataset:
# 1. Print shape
print(ml_data.shape)
# 2. Print first 5 rows
print(ml_data.head(5))
# 3. Print data types
print(ml_data.dtypes)
# 4. Print statistical summary
print(ml_data.describe())
# 5. Get all scores using loc
print(ml_data.loc[:,"score"])
# 6. Get first 3 students using iloc
print(ml_data.iloc[0:3])
# 7. Get students who passed (boolean filtering)
print(ml_data[ml_data["passed"]==True])
# 8. Get students with score > 80
print(ml_data [ml_data["score"] > 80])
# 9. Get study_hours and score columns only
print(ml_data[["study_hours","score"]])
# 10. Print: "X out of Y students passed"
total=len(ml_data)
passed=ml_data["passed"].sum()
print(f"{passed} out of {total} students passed")
























# Q10. Dictionary to ML pipeline:
# You have model results as dictionary
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




# lambda = mini function without a name


# Finding best item in dictionary by value:
best = max(my_dict, key=lambda x: my_dict[x]["some_value"])