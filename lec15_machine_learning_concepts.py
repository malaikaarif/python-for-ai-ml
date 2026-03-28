# Lecture 15: Introduction to Machine Learning

# Logistic Regression (Classification Example)
# --------------------------------------------------------
# Goal:
# Predict whether a student will PASS or FAIL based on study hours


# Import Logistic Regression model
from sklearn.linear_model import LogisticRegression


# --------------------------------------------------------
# Step 1: Create dataset

data = {
    'study_hours': [1, 2, 3, 4, 5, 6],   # Input feature (independent variable)
    'result': [0, 0, 0, 1, 1, 1]         # Output (dependent variable)
}

# Convert data into X (inputs) and y (outputs)

# X must be 2D (list of lists)
x = [[hour] for hour in data['study_hours']]

# y is the target (labels)
y = data['result']


# --------------------------------------------------------
# Step 2: Create and train model

model = LogisticRegression()

# Train the model using data
model.fit(x, y)


# --------------------------------------------------------
# Step 3: Make predictions

predictions = model.predict([[3.5], [5.5]])


# --------------------------------------------------------
# Step 4: Display results

print(f"Prediction for 3.5 hours: {'Pass' if predictions[0] == 1 else 'Fail'}")
print(f"Prediction for 5.5 hours: {'Pass' if predictions[1] == 1 else 'Fail'}")