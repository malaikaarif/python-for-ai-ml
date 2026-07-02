# ============================================
# DataCamp - Chapter 3 - PRACTICE
# ============================================

# ===== LEVEL 1: BUILT-IN FUNCTIONS =====

# Q1. Predict the output WITHOUT running:
print(max(1, 5, 3, 9, 2))                  # 9
print(min(1, 5, 3, 9, 2))                  # 1
print(round(3.14159, 3))                   # 3.141
print(round(3.14159))                      # 3
print(len([1, 2, 3, 4, 5]))                # 5
print(abs(-99))                            # 99








# Q2. What's the bug and fix it:
numbers = [3, 1, 4, 1, 5, 9]
# Separate variables = better for debugging
biggest = max(numbers)
smallest = min(numbers)
total = sum(numbers)
average = sum(numbers) / len(numbers)
print(f"Max: {biggest}, Min: {smallest}, Total: {total}, Avg: {average:.2f}")




# don't need to introduce separate variables for the list - it can work directly
numbers = [3,1,4,1,5,9]
max(numbers)
min(numbers)
sum(numbers)

print(f"Max: {max(numbers)}, Min: {min(numbers)} sum: {sum(numbers)} Avg: {sum(numbers)/len(numbers):.2f}")





# ===== LEVEL 2: ARGUMENTS =====

# Q3. Predict the output:
print(round(3.7777, 2))                     # 3.78
print(round(ndigits=2, number=3.7777))  # keyword args              # 3.78
print(round(3.7777, ndigits=2))         # mixed                     # 3.78









# Q4. What's the difference?
# a) round(3.5)                # 4
# b) round(3.5, 0)             # 4.0
# Predict both outputs and explain why they might differ!

# no digits = returns integer
# n-digits = 0 = returns floaat








# ===== LEVEL 3: METHODS =====

# Q5. Predict WITHOUT running:
name = "malaika arif"
print(name.upper())                 # MALAIKA ARIF
print(name.capitalize())            # Malaika arif
print(name.replace("a", "@"))       # m@l@ik@ @rif
print(name.count("a"))              # 4
print(name.split(" "))              # ['malaika','arif']
print(len(name.split(" ")))   # careful! 🤔       2






# Q6. What's the bug? Fix it:
sentence = "  hello world  "                    # no need to add space
result = sentence.strip()                       # then it removes space
words = result.split(" ")                       # then it made list of 2 words
first_word = words[0].upper()                   
print(first_word)

# i think there is no need to add extra space while defining sentence
# overall the code is working


# NLP preprocessing works in real ML:
# Real tweet cleaning pipeline:

#tweet = "  I LOVE Python!  "
#tweet = tweet.strip()     # remove whitespace
#tweet = tweet.lower()     # normalize case
#tweet = tweet.split(" ")  # tokenize into words




# Q7. Predict the output:
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(nums.count(1))           # 2
print(nums.index(5))           # 4
nums.append(7)                 
print(nums)                    # [3,1,4,1,5,9,2,6,7]
nums.remove(1)     # careful! which 1 gets removed?         the 1 from the start
print(nums)

# [3,4,1,5,9,2,6,7]

# .index(5) → "where is the value 5?" → returns 4 (its position)
# nums[5] → "what's at position 5?" → returns 9








# Q8. THE IN-PLACE TRAP - predict:
nums = [3, 1, 2]
result = nums.sort()
print(result)      # what prints here?         nothing         (sort() modifies in place, returns nothing)
print(nums)        # what prints here?         [1,2,3]

name = "malaika"
result2 = name.upper()
print(result2)     # what prints here?       MALAIKA
print(name)        # what prints here?       malaika           strings are immutable, original unchanged

# .upper() doesn't change the original string, it returns a new string!









# ===== LEVEL 4: PACKAGES =====

# Q9. Fix the import errors:
# Error 1:

# numpy.array([1,2,3])    # missing something!

# import numpy as np
# np.array([1,2,3])

# or

from numpy import array as arr
arr([1,2,3])

# Error 2:
# from math import pi, sqrt
# print(math.pi)          # why is this wrong?     no need to write math.pi becoz we already imported pi library

# Error 3:
# import matplotlib.pyplot as plt
# plot([1,2,3])           # why is this wrong?            need to wrote plt.plot([1,2,3])






# Q10. Write the correct import for each:
# 1. Import numpy with alias np          import numpy as np
# 2. Import pandas with alias pd         import pandas as pd
# 3. Import only sqrt from math          from math import sqrt
# 4. Import pyplot from matplotlib with alias plt          import matplotlib.pyplot as plt
# 5. Import train_test_split from sklearn.model_selection        from sklearn.model_selection import train_test_split







# ===== LEVEL 5: AI/ML CHALLENGE =====

# Q11. Text preprocessing (NLP style):
tweet = "  I LOVE Machine Learning!!! It's AMAZING!  "

# Using string methods:
# 1. Remove whitespace from both ends
# 2. Convert to lowercase
# 3. Replace "!!!" with ""
# 4. Split into individual words
# 5. Count how many words
# 6. Print: "Tweet has X words after cleaning"
# Do it step by step with proper variable names!




step1=tweet.strip()
print(step1)

step2=step1.lower()
print(step2)

step3=step2.replace("!!!","")
print(step3)

step4=step3.split(" ")
print(step4)

step5=len(step4)

print(f"Tweet has {step5} words after cleaning.")



# count() counts occurrences of a character/substring. len() counts items in a list! 

# This sequential pipeline concept is exactly how real NLP preprocessing works in ML:
# Real world ML text pipeline:
# text → strip → lowercase → remove punctuation → split → vectorize → model











# Q12. Dataset stats:
model_accuracies = [0.87, 0.92, 0.78, 0.95, 0.88, 0.91, 0.76, 0.93]

# Using built-in functions:
# 1. Best accuracy
# 2. Worst accuracy
# 3. Total sum
# 4. Average accuracy
# 5. Number of models tested
# 6. Print a summary:
#    "Tested X models. Best: X%, Worst: X%, Average: X%"
#    (multiply by 100 and round to 1 decimal for percentages)


step1 = max(model_accuracies)
print(step1)

step2 = min(model_accuracies)
print(step2)

step3 = sum(model_accuracies)
print(step3)


# average
step4 = step3/len(model_accuracies)

step5 = len(model_accuracies)
print(step5)

print(f"Tested {step5} models. Best: {step1*100:.1f} , Worst: {step2*100:.1f} , Average: {step4*100:.1f}" )

