# Lecture 14: Normalization & Standardization
# -------------------------------------------------------------
# Topics Covered:
# 1. Creating dataset using Pandas
# 2. Normalization using MinMaxScaler
# 3. Standardization using StandardScaler
# 4. Converting scaled data back to DataFrame


# Import required libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler


# -------------------------------------------------------------
# Step 1: Create dataset

data = pd.DataFrame({
    'Feature1': [10, 20, 30, 40, 50],
    'Feature2': [1, 2, 3, 4, 5]
})

# Display original dataset
print("Original Dataset:")
print(data)


# -------------------------------------------------------------
# Step 2: Normalization (Min-Max Scaling)

# Create MinMaxScaler object
scaler = MinMaxScaler()

# Fit the data and transform it (scale values between 0 and 1)
normalized_data = scaler.fit_transform(data)

# Convert scaled data back to DataFrame for better readability
print("\nNormalized Dataset: Scaled to range [0,1]")
print(pd.DataFrame(normalized_data, columns=data.columns))


# -------------------------------------------------------------
# Step 3: Standardization (Z-score Scaling)

# Create StandardScaler object
scaler = StandardScaler()

# Fit and transform the data (mean = 0, std = 1)
standardized_data = scaler.fit_transform(data)

# Convert scaled data back to DataFrame
print("\nStandardized Dataset: Mean = 0, Std = 1")
print(pd.DataFrame(standardized_data, columns=data.columns))