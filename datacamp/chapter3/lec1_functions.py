# ============================================
# DataCamp - Chapter 3 - Functions & Packages
# COMPLETE NOTES
# ============================================

# ===== 1. WHAT IS A FUNCTION? =====
# A function = reusable, standalone block of code
# Takes input (arguments) → does something → returns output

print(max(1, 5, 3))      # built-in function
print(round(3.14159, 2)) # → 3.14
print(type(5))           # type() is also a function!






# ===== 2. help() FUNCTION =====
# Shows documentation - what arguments a function takes
help(round)
help(max)
help(print)

# ⚠️ AI/ML use: Use help() CONSTANTLY when learning new
# library functions (numpy, pandas, sklearn etc.)





# ===== 3. ARGUMENTS - POSITIONAL vs KEYWORD =====

# Positional - order matters
round(3.14159, 2)        # number=3.14159, ndigits=2 (by position)

# Keyword - you name the argument, order doesn't matter
round(number=3.14159, ndigits=2)
round(ndigits=2, number=3.14159)   # same result!

# Multiple arguments
print(max(1, 5, 3, 9, 2))   # → 9

# Default arguments (functions can have defaults)
round(3.14159)      # ndigits defaults to 0 → 3
round(3.14159, 2)   # ndigits explicitly given → 3.14







# ===== 4. FUNCTIONS vs METHODS =====
# Function: standalone, called directly
len("hello")
type(5)
print("hi")

# Method: belongs to an object, uses DOT notation
"hello".upper()       # string method
[1,2,3].append(4)     # list method
"hello".capitalize()







# ===== 5. STRING METHODS =====
name = "malaika arif"

print(name.capitalize())  # → "Malaika arif" (only first letter)
print(name.upper())       # → "MALAIKA ARIF"
print(name.lower())       # → "malaika arif"
print(name.replace("a", "@"))  # → "m@l@ik@ @rif"
print(name.count("a"))    # → counts occurrences
print(name.index("arif")) # → position of substring
print(name.strip())       # removes whitespace from ends
print(name.split(" "))    # → ["malaika", "arif"] (splits into list!)

# ⚠️ AI/ML use: 
# .split() used CONSTANTLY in NLP text preprocessing
# .lower() used to normalize text before feeding to models






# ===== 6. LIST METHODS =====
nums = [3, 1, 4, 1, 5, 9]

nums.append(2)        # adds to end → [3,1,4,1,5,9,2]
nums.remove(1)        # removes FIRST occurrence of value 1
nums.reverse()         # reverses list in place
nums.sort()            # sorts list in place
print(nums.index(4))   # finds position of value 4
print(nums.count(1))   # counts occurrences of 1

# ⚠️ IMPORTANT: These methods modify list IN PLACE
# They don't return a new list, they return None!
nums = [3, 1, 2]
result = nums.sort()
print(result)    # → None !!! (common bug)
print(nums)      # → [1, 2, 3] (the actual sorted list)






# ===== 7. PACKAGES (IMPORTING) =====

# Method 1 - import whole package
import numpy
numpy.array([1,2,3])

# Method 2 - import with alias (MOST COMMON in AI/ML)
import numpy as np
np.array([1,2,3])

# Method 3 - import specific function only
from math import pi
print(pi)            # use directly, no "math." needed

# Method 4 - import multiple specific functions
from math import pi, sqrt
print(sqrt(16))

# ⚠️ AI/ML STANDARD IMPORTS (memorize these!):
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# ===== KEY TAKEAWAYS FOR AI/ML =====
# 1. help() - use constantly to learn new library functions
# 2. .split() and .lower() - core NLP preprocessing
# 3. List methods modify IN PLACE - don't expect a return value
# 4. import numpy as np - literally how every ML script starts
# 5. Keyword arguments make code more readable (use them!)




# ⚠️ METHODS THAT MODIFY IN PLACE vs RETURN NEW VALUE

# These RETURN something (don't modify original):
name = "malaika"
name.upper()          # returns "MALAIKA" but doesn't change `name`!
print(name)            # still "malaika" ❌ bug if you expected uppercase!

name = name.upper()    # ✅ must reassign!
print(name)             # → "MALAIKA"

# These MODIFY IN PLACE (list methods):
nums = [3, 1, 2]
nums.sort()             # modifies nums directly
print(nums)              # → [1, 2, 3] ✅ no reassignment needed




# ===== MORE WAYS TO IMPORT (completing the list) =====

# Import with custom alias for specific function too
from numpy import array as arr
arr([1,2,3])

# Importing everything (NOT recommended - bad practice)
from math import *
print(pi)     # works, but messy - avoid this in real code!

# ⚠️ Why avoid "import *"?
# It pollutes your namespace - if math.py and numpy both have
# a function called "sqrt", you won't know which one you're using!





# # 1. sorted() vs .sort()
nums = [3, 1, 2]
sorted_nums = sorted(nums)  # returns NEW list, original unchanged
nums.sort()                  # modifies IN PLACE, returns None

# sorted() works on ANY iterable, .sort() only on lists
print(sorted("malaika"))   # → ['a', 'a', 'a', 'i', 'k', 'l', 'm']





# 2. str() and int() are also functions!
print(str(99))      # → "99"
print(int("99"))    # → 99
print(float("3.14"))# → 3.14





# 3. print() has extra arguments you didn't know!
print("a", "b", "c")              # → a b c
print("a", "b", "c", sep="-")     # → a-b-c
print("a", "b", "c", sep="")      # → abc
print("hello", end=" ")           # no newline at end!
print("world")                     # → hello world (same line!)




# 4. input() function (basic but useful)
name = input("Enter your name: ")
print(f"Hello {name}!")




# 5. String method you missed - startswith/endswith
filename = "model_weights.pkl"
print(filename.endswith(".pkl"))    # → True (useful for file handling!)
print(filename.startswith("model")) # → True





# 6. join() - opposite of split() - VERY important in NLP!
words = ["I", "love", "Python"]
sentence = " ".join(words)          # → "I love Python"
sentence2 = "-".join(words)         # → "I-love-Python"




# sorted() vs .sort()
# print(sep=, end=)
# .join() — opposite of split, used everywhere in NLP
# .endswith() and .startswith() — used in file handling