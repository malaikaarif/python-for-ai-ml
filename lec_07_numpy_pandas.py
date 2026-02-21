# Lecture 07: NumPy and Pandas Basics
# Topics covered:
# 1. Creating NumPy arrays
# 2. Performing operations on arrays
# 3. Creating Pandas DataFrame
# 4. Accessing columns and rows


# Import libraries
import numpy as np
import pandas as pd


# -----------------------------------------
# NumPy Example

# Create NumPy array
data = np.array([1, 2, 3, 4, 5])

# Display array
print("Original Array:", data)

# Multiply array elements
print("Array multiplied by 2:", data * 2)

# Sum of array elements
print("Sum of array:", np.sum(data))


# -----------------------------------------
# Pandas Example

# Create dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 70000, 60000]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print("\nDataFrame:")
print(df)

# Access Name column
print("\nName Column:", df["Name"].tolist())

# Access first row using iloc
print("\nFirst Row:")
print(df.iloc[0])
