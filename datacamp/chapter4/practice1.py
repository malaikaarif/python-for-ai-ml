# ============================================
# DataCamp - Chapter 4 - NumPy PRACTICE
# ============================================

import numpy as np

# ===== LEVEL 1: BASICS =====

# Q1. Predict the output WITHOUT running:
arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)                             # [2,4,6,8,10]
print(arr + 10)                            # [11,12,13,14,15]
print(arr ** 2)                            # [1,4,9,16,25]
print(arr > 3)                             # it will print some boolean values - to print exact we use print(arr[arr>3])
print(type(arr))                           # numpy.ndarray









# Q2. What happens here? Predict dtype:
arr1 = np.array([1, 2, 3])
arr2 = np.array([1.0, 2.0, 3.0])
arr3 = np.array([1, 2.0, 3])
arr4 = np.array([1, 2, "three"])

print(arr1.dtype)                 # int64
print(arr2.dtype)                 # float64
print(arr3.dtype)                 # flaot64   
print(arr4.dtype)                 # string        --- <U21 (unicode string)
print(arr4)        # what does it look like?            # ['1','2','three']




# NLP (Natural Language Processing) uses unicode strings
# When you load text data → dtype will be <U...
# You need to convert to numbers before feeding to model!

# Example:
labels = np.array(["cat", "dog", "cat", "bird"])
print(labels.dtype)   # → <U4 (unicode)
# ML model can't use strings → must encode to numbers!










# ===== LEVEL 2: OPERATIONS & BOOLEAN INDEXING =====

# Q3. Predict WITHOUT running:
import numpy as np
heights = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
weights = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

bmi = weights / heights ** 2
print(bmi)
print(bmi > 23)                                                # print boolean values
print(bmi[bmi > 23])    # ← what does this give?               # 24.7473475











# Q4. Boolean indexing challenge:
import numpy as np
scores = np.array([45, 67, 89, 34, 78, 92, 55, 71, 88, 63])

# Write code to:
# 1. Print all scores above 70     
print(scores[scores > 70])
# 2. Print all scores below 50
print(scores[scores < 50])
# 3. How many scores are above 70? (hint: use len() or sum())
length = len(scores[scores > 70])
print(length)

# 4. Print: "X students passed (score > 70)"
print(f"{length} students passed (score > 70)")



# ✅ Fix 2 - using sum() (more NumPy style!)
length = np.sum(scores > 70)
# True=1, False=0 → sum counts the Trues!


predictions,image=1                   # just assume
# This np.sum(condition) trick is used constantly in ML:
# How many predictions were correct?
correct = np.sum(predictions == labels)
# How many pixels are bright?
bright = np.sum(image > 0.5)










# ===== LEVEL 3: 2D ARRAYS =====

# Q5. Predict the output:
import numpy as np
np_2d = np.array([[1.73, 65.4],
                   [1.68, 59.2],
                   [1.71, 63.6],
                   [1.89, 88.4],
                   [1.79, 68.7]])

print(np_2d.shape)                     # (5,2) 5 rows , 2 cols
print(np_2d[0])                        # [1.73, 65.4]
print(np_2d[0, 0])                     # [1.73]
print(np_2d[:, 0])                     # print all rows and 1st col    
print(np_2d[:, 1])                     # print all rows and 2nd col
print(np_2d[1, :])                     # print first row and all cols
print(np_2d[0:3, 0:2])                 # print 0 to 2 rows and o to 1 col

# i don't know how to write - i just explain the logic 

np_2d[0:3, 0:2]
# rows 0,1,2 → first 3 rows
# cols 0,1 → both columns (only 2 cols exist!)
# so gives first 3 complete rows!










# Q6. 2D array challenge:
import numpy as np
dataset = np.array([[85, 92, 78],
                    [90, 88, 95],
                    [72, 68, 80],
                    [95, 97, 92]])

# 1. What is the shape?
print(dataset.shape)             # (4,3)

# 2. Get first student's all scores
print(dataset[0])                # [85 92 78]
 
# 3. Get all students' first score (column 0)
print(dataset[:,0])              # [85 90 72 95]

# 4. Get last 2 students' data
print(dataset[2:4,0:4])              # [[72 68 80] [95 97 92]]              print(dataset[2:, :])   # no need to hardcode 4, : means all cols

# 5. Get scores of students 2 and 3 (index 1 and 2)
print(dataset[1:3, 0:4])             # [[90 88 95][72 68 80]]

# 6. What is the highest score in entire dataset?
print(np.max(dataset))               # 97

# 7. What is average score per student? (hint: axis=1)
print (np.mean(dataset))                          # gives ONE average for entire dataset!

# ✅ Correct - axis=1 means average ACROSS columns (per row/student)
print(np.mean(dataset, axis=1))   # → [85. 91. 73.33 94.67]




# axis concept   - This axis concept is asked in EVERY ML interview! 💡

dataset = [[85, 92, 78],   # student 1 average = (85+92+78)/3
           [90, 88, 95],   # student 2 average = (90+88+95)/3
           [72, 68, 80],   # student 3 average = (72+68+80)/3
           [95, 97, 92]]   # student 4 average = (95+97+92)/3

np.mean(dataset, axis=0)  # average per COLUMN (per exam)
np.mean(dataset, axis=1)  # average per ROW (per student) ✅



# axis=0 → column-wise operation (across all samples)
# axis=1 → row-wise operation (across all features)













# ===== LEVEL 4: STATISTICS =====

# Q7. mean vs median — predict and explain:

# while finding median, first sort the data

import numpy as np
clean_data = np.array([170, 175, 168, 172, 169])
outlier_data = np.array([170, 175, 168, 172, 500])

print(np.mean(clean_data))               # 170.8
print(np.median(clean_data))             # [168,169,170,172,175]          170
print(np.mean(outlier_data))             # 237
print(np.median(outlier_data))           # [168,170,172,175,500]          172

# Why is median better when outliers exist?
# Write your answer as a comment!

# outlier exists when mean > median - outlier is high value far from origin while median is mid value near to origin
# that's why median better when outliers exist

# median always exist, outlier may or may not



# Better explanation:
# Mean adds ALL values then divides - so ONE huge outlier
# pulls the mean dramatically (500 pulled mean from 170 to 237!)

# Median just finds the MIDDLE value - outlier can be
# as big as possible but middle value stays the same!

# Rule: mean >> median → outliers present!
# In ML: always plot both before choosing which to use!




# Mean  = sum / count → sensitive to outliers
# Median = middle value after sorting → NOT sensitive to outliers




# Mean → affected by outliers (500 pulled mean from 170 to 237!)
# Median → NOT affected (still 172, outlier doesn't matter!)

# Real ML rule:
# If mean >> median → outliers present → use median!
# If mean ≈ median → no outliers → either works!












# Q8. Statistics challenge:

import numpy as np
exam_scores = np.array([78, 85, 92, 67, 88, 73, 95, 81, 76, 89])

# Calculate:
# 1. Mean score
mean=np.mean(exam_scores)
print(mean)

# 2. Median score
median=np.median(exam_scores)
print(median)

# 3. Standard deviation
std_score=np.std(exam_scores)
print(std_score)

# 4. Highest score
max_score=np.max(exam_scores)
print(max_score)

# 5. Lowest score
min_score=np.min(exam_scores)
print(min_score)

# 6. Are mean and median close? What does that tell you?
# mean is 82.4 and median is 83 -- difference of 0.6 almost close
# This tells us: NO significant outliers in data
# Distribution is fairly symmetric!


# 7. Print summary:
#    "Mean: X | Median: X | Std: X | Range: X"
#    (range = max - min)


range_score=max_score-min_score
print(f"Mean: {mean:.1f} | Median: {median:.1f} | Std: {std_score:.1f} | Range: {range_score:.1f} ")



# NEVER use Python built-in names as variables!
# max, min, list, dict, type, sum, range, id
# These are all reserved — overwriting them causes silent bugs!











# ===== LEVEL 5: AI/ML CHALLENGE =====

#  real ML tasks — image data and dataset preprocessing

# Q9. Image data challenge (MNIST style):
# Single image = 28x28 pixels
import numpy as np
image = np.random.rand(28, 28)  # random pixel values 0-1

# 1. What is the shape?
print(image.shape)

# 2. Total number of pixels?
print(image.size)
print(image.shape[0]*image.shape[1])

# 3. Get first row of pixels
print(image[0])

# 4. Get pixel at position (0, 0)
print(image[0][0])

# 5. Get center 4x4 region (rows 12-16, cols 12-16)
print(image[12:16,12:16])

# 6. What is mean pixel value?
mean=np.mean(image)
print(mean)

# 7. How many pixels are above 0.5?
x=np.sum(image > 0.5)
print(x)

# 8. Reshape to 1D array (784 pixels) — used when feeding to ML model!
print(image.reshape(784))

# 9. Print: "Image has X pixels, mean brightness: X"
print(f"Image has {image.size} pixels, mean brightness is {mean:.4f}")














# Q10. Dataset preprocessing challenge:
# You have a dataset of house prices
import numpy as np
np.random.seed(42)
prices = np.array([250000, 380000, 150000, 520000, 290000,
                   410000, 175000, 340000, 1200000, 310000])

# 1. Check mean vs median — are there outliers?
print(np.mean(prices))

print(np.median(prices))                # mean is greater than median so there r outliers

# 2. Find the outlier (price > 800000)

print(prices[prices > 800000])

# 3. Remove the outlier and store as clean_prices
clean_prices= prices[prices < 800000]
print(clean_prices)


# 4. Recalculate mean and median of clean_prices
print(np.mean(clean_prices))
print(np.median(clean_prices))


# 5. Normalize prices to 0-1 range:
min_prices = np.min(clean_prices)
max_prices = np.max(clean_prices)
normalized = (clean_prices - min_prices) / (max_prices - min_prices)



# 6. Print: "Original mean: X | Clean mean: X | Difference: X"
diff= abs(np.mean(clean_prices) - np.mean(prices))
print(f"Original mean: {np.mean(prices):.0f} | Clean mean: {np.mean(clean_prices):.0f} | Difference: {diff:.0f}")