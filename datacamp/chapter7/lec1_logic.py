# ============================================
# Intermediate Python - Chapter 3
# Logic, Control Flow and Filtering - COMPLETE NOTES
# ============================================

import numpy as np
import pandas as pd

# ===== 1. COMPARISON OPERATORS =====
# These return True/False - foundation of all filtering!

# ----- Equality -----
print(2 == 2)                  # → True
print("hello" == "hello")      # → True
print("hello" == "Hello")      # → False (case-sensitive!)
print(2 != 3)                  # → True




# ----- Greater and less than -----
print(3 < 5)     # → True
print(3 <= 3)    # → True (<=, >= include "equal to")
print(5 > 3)     # → True
print(5 >= 5)    # → True



# ⚠️ Comparing different types → TypeError!
# print(3 < "4")   # ❌ TypeError: can't compare int and str

# ----- Compare arrays -----
bmi = np.array([21.852, 20.975, 21.750, 24.747, 21.441])
print(bmi > 21)
# → array([ True, False,  True,  True,  True])

# ⚠️ KEY INSIGHT: comparing an array to a number applies the
# comparison to EVERY element → returns an array of booleans.
# This is called "vectorized comparison" - the backbone of
# data filtering in AI/ML.






# ===== 2. BOOLEAN OPERATORS =====

# ----- and, or, not (1) - on single values -----
x = 8
y = 15
print(x > 5 and y > 5)     # → True  (BOTH must be true)
print(x > 5 or y > 100)    # → True  (only ONE needs to be true)
print(not x > 5)           # → False (flips True → False)

# ----- and, or, not (2) - more practice -----
my_kitchen = 18.0
your_kitchen = 14.0
print(my_kitchen > 10 and my_kitchen < 18)   # → False (18 not < 18)
print(my_kitchen * 2 < your_kitchen * 3)     # → depends on values

# ----- Boolean operators with NumPy -----
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# ❌ WRONG - plain and/or/not do NOT work on arrays:
# my_house > 18 and your_house > 18
# → ValueError: truth value of an array is ambiguous

# ✅ RIGHT - use NumPy's logical functions:
print(np.logical_and(my_house > 18, your_house > 18))
print(np.logical_or(my_house > 18, your_house > 18))
print(np.logical_not(my_house > 18))

# ⚠️ WHY: plain and/or/not only work on ONE True/False value.
# An array comparison gives back MANY True/False values at once,
# so Python can't collapse it into a single decision.
# np.logical_and/or/not compare ELEMENT-BY-ELEMENT instead.


# ===== 3. if, elif, else =====

# ----- Warmup / if -----
z = 4
if z % 2 == 0:
    print("z is even")

# ----- Add else -----
z = 5
if z % 2 == 0:
    print("z is even")
else:
    print("z is odd")

# ----- Customize further: elif -----
z = 3
if z % 2 == 0:
    print("z is divisible by 2")
elif z % 3 == 0:
    print("z is divisible by 3")
else:
    print("z is neither divisible by 2 nor 3")

# ⚠️ KEY RULE: Python checks top to bottom and STOPS at the
# first True condition - it does NOT check the rest, even if
# they would also be True.






# ===== 4. FILTERING PANDAS DATAFRAMES =====
# The real payoff - combining boolean logic + DataFrames!

cars = pd.DataFrame({
    "cars_per_cap": [809, 731, 588, 18, 200, 70, 45],
    "country": ["US", "AUS", "JPN", "IN", "RU", "MOR", "EG"],
    "drives_right": [True, False, False, False, True, True, True]
})

# ----- Filtering pandas DataFrames (intro pattern) -----
# 3-step process:
dr = cars["drives_right"]        # Step 1: select column → boolean Series
sel = cars[dr]                   # Step 2&3: use it to filter
print(sel)

# ----- Driving right (1) - with intermediate variable -----
dr = cars["drives_right"]
sel = cars[dr]
print(sel)

# ----- Driving right (2) - one-liner version -----
sel = cars[cars["drives_right"]]
print(sel)

# ----- Cars per capita (1) - numeric condition -----
cpc = cars["cars_per_cap"]
many_cars = cpc > 500
car_maniac = cars[many_cars]
print(car_maniac)

# ----- Cars per capita (2) - combining two conditions -----
cpc = cars["cars_per_cap"]
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]
print(medium)

# Alternative pandas syntax (using & instead of np.logical_and):
medium2 = cars[(cars["cars_per_cap"] > 100) & (cars["cars_per_cap"] < 500)]
print(medium2)
# ⚠️ With pandas use & / | / ~ (NOT and/or/not), and ALWAYS
# wrap each condition in its own parentheses.







# ===== 5. BONUS: Not in this DataCamp chapter, but you'll need these =====
# (These build directly on what you just learned)

# ----- Ternary / conditional expression -----
# A compact one-line if/else - very common in ML preprocessing code
age = 20
status = "adult" if age >= 18 else "minor"
print(status)   # → "adult"





# ----- Chained comparisons (Python-only trick) -----
z = 10
print(5 < z < 15)   # → True (same as: 5 < z and z < 15)





# ----- any() and all() -----
# Useful when you have a boolean array/Series and want ONE final answer
scores = np.array([45, 78, 92, 60, 88])
print((scores > 70).any())   # → True  - "is at least one score > 70?"
print((scores > 70).all())   # → False - "are ALL scores > 70?"






# ----- .isin() - filter by a list of values (super common in real datasets) -----
cars_subset = cars[cars["country"].isin(["US", "JPN", "EG"])]
print(cars_subset)

# ----- .between() - cleaner alternative to writing two conditions -----
mid_range = cars[cars["cars_per_cap"].between(100, 500)]
print(mid_range)

# ----- df.query() - filter using a string expression (nice for readability) -----
filtered = cars.query("cars_per_cap > 100 and cars_per_cap < 500")
print(filtered)


# ===== KEY TAKEAWAYS FOR AI/ML =====
# 1. Array comparisons (bmi > 21) → return boolean arrays, used everywhere in preprocessing
# 2. Plain and/or/not → ONLY for single values, NEVER for arrays/columns
# 3. np.logical_and / np.logical_or / np.logical_not → for combining array conditions
# 4. pandas equivalent → & , | , ~ with parentheses around each condition
# 5. if/elif/else → stops at first True match, used for labeling & custom logic
# 6. df[condition] → the single most-used pattern in ML data cleaning
# 7. df[cond1 & cond2] → compound filtering, how you'll split/clean real datasets
# 8. any()/all(), .isin(), .between(), .query() → real-world shortcuts you'll
#    see constantly once you move past textbook examples into actual datasets