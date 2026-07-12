# ============================================
# Intermediate Python - Chapter 2
# Dictionaries & Pandas - COMPLETE NOTES
# ============================================

import pandas as pd
import numpy as np

# ===== 1. WHY DICTIONARIES? =====
# Problem with lists - need two lists and index matching:
countries = ["spain", "france", "germany"]
capitals  = ["madrid", "paris", "berlin"]
# To find capital of france:
ind_france = countries.index("france")  # → 1
print(capitals[ind_france])             # → "paris" ← messy!

# Dictionary solves this - direct key access:
capitals = {"spain": "madrid",
            "france": "paris",
            "germany": "berlin"}
print(capitals["france"])  # → "paris" ✅ clean!

# ===== 2. DICTIONARY BASICS =====
# Structure: {key: value, key: value}
# Keys   → must be UNIQUE and IMMUTABLE (string, int, tuple)
# Values → can be ANYTHING (string, int, list, dict!)

# Creating dictionary
person = {"name": "Malaika",
          "age": 22,
          "is_student": True,
          "scores": [85, 90, 92]}  # value can be a list!

# ===== 3. ACCESSING DICTIONARY =====
print(person["name"])      # → "Malaika"
print(person["scores"])    # → [85, 90, 92]

# Check if key exists BEFORE accessing!
print("name" in person)    # → True
print("salary" in person)  # → False

# ⚠️ Accessing non-existent key → KeyError!
# print(person["salary"])  # → KeyError!
# Safe way:
print(person.get("salary", "Not found"))  # → "Not found"

# ===== 4. DICTIONARY MANIPULATION =====
capitals = {"spain": "madrid", "france": "paris"}

# ADD new key-value pair
capitals["italy"] = "rome"
print(capitals)  # → {"spain":"madrid","france":"paris","italy":"rome"}

# UPDATE existing value
capitals["spain"] = "MADRID"
print(capitals["spain"])  # → "MADRID"

# DELETE entry
del capitals["france"]
print(capitals)  # → {"spain":"MADRID","italy":"rome"}

# ===== 5. DICTIONARY METHODS =====
capitals = {"spain": "madrid", "france": "paris", "italy": "rome"}

print(capitals.keys())    # → dict_keys(['spain','france','italy'])
print(capitals.values())  # → dict_values(['madrid','paris','rome'])
print(capitals.items())   # → dict_items([('spain','madrid'),...])

# Loop through dictionary
for key, value in capitals.items():
    print(f"{key}: {value}")

# ===== 6. NESTED DICTIONARIES =====
# Dictionary inside dictionary!
europe = {
    "spain": {"capital": "madrid", "population": 47},
    "france": {"capital": "paris", "population": 67},
    "germany": {"capital": "berlin", "population": 83}
}

# Access nested - use TWO keys!
print(europe["spain"])              # → {"capital":"madrid","population":47}
print(europe["spain"]["capital"])   # → "madrid"
print(europe["france"]["population"]) # → 67

# Add nested
europe["italy"] = {"capital": "rome", "population": 60}

# ⚠️ AI/ML use:
# Model config stored as nested dict:
config = {
    "model": {"layers": 3, "units": 128},
    "training": {"epochs": 10, "lr": 0.001}
}
print(config["training"]["lr"])   # → 0.001

# ===== 7. PANDAS DATAFRAME =====
# DataFrame = Excel spreadsheet in Python!
# Rows = observations (samples)
# Columns = features
# Can hold MIXED data types!

# ===== 8. CREATING DATAFRAMES =====

# Way 1: From dictionary
data = {
    "name": ["Alice", "Bob", "Sara", "John"],
    "age": [25, 30, 22, 28],
    "salary": [50000, 60000, 45000, 55000],
    "city": ["NYC", "LA", "NYC", "Chicago"]
}
df = pd.DataFrame(data)
print(df)
#     name  age  salary     city
# 0  Alice   25   50000      NYC
# 1    Bob   30   60000       LA
# 2   Sara   22   45000      NYC
# 3   John   28   55000  Chicago

# Way 2: From CSV file (most common in real ML!)
# df = pd.read_csv("data.csv")
# df = pd.read_csv("data.csv", index_col=0)  # first col as index

# ===== 9. DATAFRAME BASICS =====
print(df.shape)     # → (4, 4) = 4 rows, 4 columns
print(df.dtypes)    # → data types of each column
print(df.head())    # → first 5 rows
print(df.head(2))   # → first 2 rows
print(df.tail())    # → last 5 rows
print(df.tail(2))   # → last 2 rows
print(df.info())    # → summary (shape, dtypes, nulls)
print(df.describe())# → stats (mean, std, min, max)

# ===== 10. CUSTOM INDEX =====
# Set custom row labels
df.index = ["alice", "bob", "sara", "john"]
print(df)
#        name  age  salary     city
# alice  Alice   25   50000      NYC
# bob      Bob   30   60000       LA
# sara    Sara   22   45000      NYC
# john    John   28   55000  Chicago

# ===== 11. SQUARE BRACKETS - Column Selection =====

# Single column → returns Series
print(df["name"])          # → Series
print(type(df["name"]))    # → pandas.Series

# Multiple columns → returns DataFrame
print(df[["name", "age"]]) # → DataFrame
print(type(df[["name", "age"]])) # → pandas.DataFrame

# ⚠️ Single brackets → Series
# ⚠️ Double brackets → DataFrame
# This difference matters in ML pipelines!

# Row selection with square brackets (slicing only!)
print(df[0:2])    # → first 2 rows
print(df[1:3])    # → rows 1 and 2

# ===== 12. loc - LABEL BASED ACCESS =====
# loc[row_label, col_label]
# INCLUSIVE on both ends!

df.index = ["alice", "bob", "sara", "john"]

# Single row
print(df.loc["alice"])              # → alice's row (Series)

# Single value
print(df.loc["alice", "name"])      # → "Alice"

# Multiple rows
print(df.loc[["alice", "bob"]])     # → 2 rows DataFrame

# Row slice
print(df.loc["alice":"sara"])       # → alice, bob, sara (INCLUSIVE!)

# All rows, specific column
print(df.loc[:, "name"])            # → all names

# All rows, multiple columns
print(df.loc[:, ["name", "age"]])   # → name and age cols

# Specific rows and columns
print(df.loc["alice":"bob", "name":"age"])  # → 2x2 subset

# ===== 13. iloc - INTEGER POSITION BASED =====
# iloc[row_number, col_number]
# EXCLUSIVE on end (like list slicing!)

# Single row by position
print(df.iloc[0])           # → first row

# Single value
print(df.iloc[0, 0])        # → "Alice" (row 0, col 0)

# Multiple rows
print(df.iloc[[0, 1]])      # → first 2 rows

# Row slice
print(df.iloc[0:2])         # → rows 0,1 only (NOT row 2!)

# All rows, specific column by position
print(df.iloc[:, 0])        # → first column

# Specific rows and columns by position
print(df.iloc[0:2, 0:2])    # → 2x2 subset

# ===== 14. loc vs iloc SUMMARY =====
# loc  → LABELS  → "alice", "name"  → INCLUSIVE end
# iloc → NUMBERS → 0, 1, 2          → EXCLUSIVE end

# Same result, different syntax:
print(df.loc["alice", "name"])  # → "Alice" (by label)
print(df.iloc[0, 0])            # → "Alice" (by position)

# ⚠️ When index is numbers (default 0,1,2...):
# loc[0:2]  → rows 0, 1, 2 (INCLUSIVE - 3 rows!)
# iloc[0:2] → rows 0, 1    (EXCLUSIVE - 2 rows!)

# ===== 15. FILTERING DATAFRAME =====
# Boolean filtering - like NumPy!
print(df[df["age"] > 25])         # rows where age > 25
print(df[df["city"] == "NYC"])    # rows where city is NYC

# Multiple conditions
print(df[(df["age"] > 25) & (df["salary"] > 50000)])

# ⚠️ AI/ML use: filtering dataset samples!
# high_accuracy = results[results["accuracy"] > 0.9]

# ===== KEY TAKEAWAYS FOR AI/ML =====
# 1. Dict → store model configs, hyperparameters
# 2. DataFrame → store and manipulate datasets
# 3. pd.read_csv() → how you load EVERY real dataset
# 4. df.head() → first thing you call on any new dataset
# 5. df.info() → check for missing values and dtypes
# 6. df.describe() → quick statistical summary
# 7. loc → use when you know column/row NAMES
# 8. iloc → use when you know column/row POSITIONS
# 9. df["col"] → Series, df[["col"]] → DataFrame
# 10. Boolean filtering → same as NumPy, used constantly!








# ===== THINGS I MISSED =====

# 1. index_col parameter in read_csv
df = pd.read_csv("data.csv", index_col=0)
# First column becomes the ROW INDEX
# Without it → pandas adds 0,1,2 as index
# ⚠️ Very common in real datasets!

# 2. Series vs DataFrame - deeper explanation
# Series = ONE column (1D)
# DataFrame = MULTIPLE columns (2D)

import pandas as pd
s = pd.Series([1, 2, 3], name="numbers")
print(type(s))          # → pandas.Series
print(s.shape)          # → (3,) = 1D!

df = pd.DataFrame({"numbers": [1, 2, 3]})
print(type(df))         # → pandas.DataFrame
print(df.shape)         # → (3, 1) = 2D!

# ⚠️ AI/ML importance:
# df["col"]   → Series  (1D) → some functions don't accept this!
# df[["col"]] → DataFrame (2D) → safer for ML pipelines!

# 3. Printing specific rows with loc/iloc
# DataCamp showed this but easy to miss:
df = pd.read_csv("cars.csv", index_col=0)

# Print first row as Series
print(df.iloc[0])        # → Series

# Print first row as DataFrame
print(df.iloc[[0]])      # → DataFrame (double brackets!)

# 4. loc with boolean Series
# Combining filtering with loc:
is_expensive = df["salary"] > 50000
print(df.loc[is_expensive])     # ← this is how DataCamp showed it!
# Same as:
print(df[df["salary"] > 50000]) # ← more common way

# 5. Printing observations and variables
# DataCamp used this terminology:
# observation = ROW (one data sample)
# variable = COLUMN (one feature)