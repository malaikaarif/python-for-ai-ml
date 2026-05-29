# Lecture 11: Data Cleaning and Transformation
# Topics covered:
# 1. Handling missing values
# 2. Removing incomplete rows
# 3. Creating new columns
# 4. Transforming text data
# 5. Saving cleaned data to CSV file


# Import Pandas library
import pandas as pd 


# -----------------------------------------
# Create messy dataset with missing values

data = pd.DataFrame({
   
   'Name': ['Alice', 'Bob', None, 'David'],   # None represents missing value
   'Age': [26, None, 21, 10],                 # Missing Age value
   'Score': [81, 93, None, 90],               # Missing Score value
   'Country': ['EdinBurgh', 'America', 'London', None]  # Missing Country value

})


# Display original messy dataset
print("Messy Dataset:")
print(data)


# -----------------------------------------
# Fill missing Name values with 'Unknown'

data['Name'].fillna('Unknown', inplace=True)


# -----------------------------------------
# Remove rows where Age or Score is missing

cleaned_data = data.dropna(subset=['Age', 'Score'])


# Display cleaned dataset
print("\nDataset after handling missing values:")
print(cleaned_data)


# -----------------------------------------
# Create new column 'Pass'
# Students with Score >= 80 are marked as True

cleaned_data['Pass'] = cleaned_data['Score'] >= 80


# -----------------------------------------
# Convert Country names to uppercase

cleaned_data['Country'] = cleaned_data['Country'].str.upper()


# Display transformed dataset
print("\nTransformed Dataset:")
print(cleaned_data)


# -----------------------------------------
# Save cleaned dataset to CSV file
# CSV stands for: Comma-Separated Values

cleaned_data.to_csv('cleaned_data.csv', index=False)

print("\nCleaned data saved to 'cleaned_data.csv'")