# Lecture 10: Data Analysis with Pandas
# Topics covered:
# 1. Creating DataFrame
# 2. Exploring dataset (shape, columns)
# 3. Descriptive statistics
# 4. Creating new columns
# 5. Filtering data


import pandas as pd


# -----------------------------------------
# Create Sample Dataset

data = pd.DataFrame({
    'Name': ['Aliyan', 'Bareera', 'Chris', 'Dawood'],
    'Age': [39, 22, 34, 26],
    'Score': [85, 83, 98, 91]
})

print("Sample Dataset:")
print(data)


# -----------------------------------------
# Basic Dataset Information

print("\nDataset Shape:", data.shape)
print("Column Names:", data.columns)


# -----------------------------------------
# Descriptive Statistics

print("\nDescriptive Statistics:")
print(data.describe())


# -----------------------------------------
# Create New Column (Pass/Fail)

data['Pass'] = data['Score'] > 80

print("\nUpdated Dataset with 'Pass' Column:")
print(data)


# -----------------------------------------
# Filter Data (Age > 30)

filtered_data = data[data['Age'] > 30]

print("\nFiltered Data (Age > 30):")
print(filtered_data)