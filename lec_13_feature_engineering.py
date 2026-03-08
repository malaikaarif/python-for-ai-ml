# Lecture 13: Feature Engineering
# --------------------------------------------------------------------



# Import pandas library for data manipulation and analysis
import pandas as pd

# Create a sample dataset with Date and Revenue columns
data = pd.DataFrame({
    'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04'],  # Date values
    'Revenue': [1000, 1500, 900, 850]  # Revenue for each day
})

# Print the original dataset
print("Original Data:")
print(data)
print("\n")


# Convert 'Date' column to datetime format and extract the day name
# This creates a new feature called 'Day'
data['Day'] = pd.to_datetime(data['Date']).dt.day_name()


# Calculate percentage change in revenue compared to the previous day
# pct_change() gives growth rate, fillna(0) replaces the first NaN with 0
data['Revenue_Growth_%'] = data['Revenue'].pct_change().fillna(0) * 100


# Create a categorical feature based on revenue value
# If revenue is >= 1000 → High, otherwise → Low
data['Revenue_Type'] = data['Revenue'].apply(lambda x: 'High' if x >= 1000 else 'Low')


# Print the transformed dataset after feature engineering
print("Transformed DataSet with new features:")
print(data)