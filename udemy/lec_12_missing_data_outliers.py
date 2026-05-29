# Lecture 12: Data Cleaning with Mean Imputation and Outlier Handling
# --------------------------------------------------------------------
# Topics Covered:
# 1. Creating dataset using Pandas
# 2. Handling missing values using mean
# 3. Handling unrealistic values using NumPy (np.where)
# 4. Displaying cleaned dataset


# Import required libraries
import pandas as pd
import numpy as np


# -----------------------------------------------------------
# Step 1: Create dataset with missing values

data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, np.nan, 30, 27],        # Missing value in Age
    "Score": [84, 90, np.nan, 91],      # Missing value in Score
})


# Display original dataset
print("Original Dataset:")
print(data)
print("\n")


# -----------------------------------------------------------
# Step 2: Handle missing values using Mean Imputation

# Replace missing Age values with mean of Age column
data['Age'] = data['Age'].fillna(data['Age'].mean())

# Replace missing Score values with mean of Score column
data['Score'] = data['Score'].fillna(data['Score'].mean())


# -----------------------------------------------------------
# Step 3: Handle unrealistic values (Outlier handling)

# If Age > 100, replace it with mean Age
data['Age'] = np.where(data['Age'] > 100, data['Age'].mean(), data['Age'])

# If Score > 100, replace it with mean Score
data['Score'] = np.where(data['Score'] > 100, data['Score'].mean(), data['Score'])


# -----------------------------------------------------------
# Step 4: Display cleaned dataset

print("Cleaned Dataset:")
print(data)