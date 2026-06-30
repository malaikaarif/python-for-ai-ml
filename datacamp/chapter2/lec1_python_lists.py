# ============================================
# DataCamp - Chapter 2 - Python Lists
# COMPLETE NOTES
# ============================================

# ===== 1. WHAT IS A LIST? =====
# List = ordered, mutable collection of items
# Can store MIXED data types unlike arrays in other languages

my_list = [1, "hello", 3.14, True]
print(my_list)
print(type(my_list))   # <class 'list'>

# ⚠️ AI/ML importance:
# A dataset row = a list
# dataset = [["Alice", 25, 1.65], ["Bob", 30, 1.80]]








# ===== 2. CREATING LISTS =====
# Empty list
empty = []

# List of same type
numbers = [1, 2, 3, 4, 5]

# Mixed types
mixed = ["Malaika", 21, True, 3.14]

# List of lists (2D - like a dataset!)
dataset = [
    ["Alice", 25, 1.65],
    ["Bob", 30, 1.80],
    ["Sara", 22, 1.55]
]








# ===== 3. INDEXING =====
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
#       0      1      2      3      4      5      6      7
#      -8     -7     -6     -5     -4     -3     -2     -1

# Positive indexing (left to right, starts at 0)
print(fam[0])    # → "liz"
print(fam[3])    # → 1.68

# Negative indexing (right to left, starts at -1)
print(fam[-1])   # → 1.89 (last element)
print(fam[-2])   # → "dad" (second from last)

# ⚠️ AI/ML importance:
# fam[-1] used constantly to get last prediction, last loss value etc.








# ===== 4. SLICING =====
# list[start:end] → includes start, EXCLUDES end

print(fam[2:5])    # → ['emma', 1.68, 'mom']
print(fam[:3])     # → first 3 elements (start defaults to 0)
print(fam[5:])     # → from index 5 to end
print(fam[:])      # → entire list (copy!)

# Negative slicing
print(fam[-3:])    # → last 3 elements
print(fam[:-2])    # → everything except last 2

# ⚠️ AI/ML importance:
# Getting last N samples from dataset:
# training_data[-1000:]  → last 1000 samples
# Splitting data:
# train = data[:800]     → first 800 rows
# test = data[800:]      → remaining rows









# ===== 5. LIST OF LISTS (2D Lists) =====
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["bedroom", 10.75]]

# Access outer list
print(house[0])          # → ["hallway", 11.25]

# Access inner element
print(house[0][1])       # → 11.25 (row 0, column 1)
print(house[2][0])       # → "bedroom"

# ⚠️ AI/ML importance:
# Neural network weights = list of lists
# Image pixels = 2D list (28x28 for MNIST)
# house[row][column] → same as matrix notation!








# ===== 6. MANIPULATING LISTS =====

# --- Replace ---
fam[7] = 1.90              # replace single element
fam[0:2] = ["lisa", 1.74]  # replace slice

# --- Add/Extend ---
fam_new = fam + ["me", 1.65]    # creates NEW list
fam_ext = fam + ["brother", 1.75, "sister", 1.60]

# --- Delete ---
del fam[2]         # delete by index
del fam[2:4]       # delete slice







# ===== 7. INNER WORKINGS - CRITICAL! ⚠️ =====
# This is the most important concept DataCamp taught!

# Lists store REFERENCES not values!
x = ["a", "b", "c"]
y = x              # y points to SAME list as x!
y[0] = "z"
print(x)           # → ["z", "b", "c"] !!!
# x changed even though we only changed y!

# Fix - use copy:
x = ["a", "b", "c"]
y = list(x)        # creates actual copy
# OR
y = x[:]           # slice copy
y[0] = "z"
print(x)           # → ["a", "b", "c"] ✅ x unchanged

# ⚠️ THIS IS CRITICAL IN AI/ML!
# Always copy lists/arrays before modifying
# Otherwise you corrupt your original dataset!

# ===== KEY TAKEAWAYS FOR AI/ML =====
# 1. Lists can hold mixed types - useful for dataset rows
# 2. Negative indexing - get last N elements easily
# 3. Slicing - split train/test data
# 4. list[row][col] - access 2D data like matrix
# 5. ALWAYS copy before modifying - never corrupt original data!








# ===== 8. SUBSETTING WITH CONDITIONS  =====

# You can subset based on calculation result
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]

# Get emma's height
emma_height = fam[fam.index("emma") + 1]







# ===== 9. LIST METHODS =====
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

numbers.index(4)     # → 2 (position of value 4)
numbers.count(1)     # → 2 (how many times 1 appears)

# ⚠️ AI/ML use:
# finding position of max value in predictions list




# 1. len() function 
fam = ["liz", 1.73, "emma"]
print(len(fam))    # → 3 (counts elements, not characters!)




# 2. in operator — checking membership
fam = ["liz", "emma", "mom"]
print("emma" in fam)      # → True
print("dad" in fam)       # → False




# ⚠️ AI/ML use: checking if a label exists in your class list
classes = ["cat", "dog", "bird"]
print("cat" in classes)   # → True




# 3. nested list mutation through reference (deeper version of Q8 bug)
matrix = [[1, 2], [3, 4]]
copy_wrong = list(matrix)   # ⚠️ this is a SHALLOW copy!
copy_wrong[0][0] = 999
print(matrix)   # → [[999, 2], [3, 4]] !!! Still changes original!


# Why? list() only copies the OUTER list
# inner lists are still shared references!

# Real fix for 2D lists:
import copy
copy_right = copy.deepcopy(matrix)