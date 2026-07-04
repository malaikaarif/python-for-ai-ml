# ============================================
# DataCamp - Chapter 4 - NumPy
# COMPLETE NOTES
# ============================================

import numpy as np

# ===== 1. WHY NUMPY? =====
# Lists can't do element-wise math:
heights = [1.73, 1.68, 1.71, 1.89]
# heights * 2   → ERROR with lists!
# heights + 2   → ERROR with lists!

# NumPy arrays CAN:
np_heights = np.array([1.73, 1.68, 1.71, 1.89])
print(np_heights * 2)    # → [3.46, 3.36, 3.42, 3.78] ✅
print(np_heights + 2)    # → [3.73, 3.68, 3.71, 3.89] ✅

# ⚠️ AI/ML importance:
# ALL ML operations = math on arrays
# Neural networks = matrix multiplications on NumPy arrays
# 50x faster than Python lists for math!







# ===== 2. CREATING NUMPY ARRAYS =====
# From list
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array)           # → [1 2 3 4 5]
print(type(my_array))     # → <class 'numpy.ndarray'>

# Directly
arr = np.array([1.5, 2.5, 3.5])







# ===== 3. NUMPY SIDE EFFECTS (TYPE COERCION) =====
# NumPy arrays can only hold ONE data type!
# If mixed → converts everything to most general type

arr1 = np.array([1, 2, 3])
print(arr1.dtype)          # → int64

arr2 = np.array([1.0, 2.0, 3.0])
print(arr2.dtype)          # → float64

# Mixed int and float → all become float
arr3 = np.array([1, 2.0, 3])
print(arr3)                # → [1. 2. 3.] (all float!)
print(arr3.dtype)          # → float64

# Mixed int and string → all become string ⚠️
arr4 = np.array([1, 2, "three"])
print(arr4)                # → ['1' '2' 'three'] (all string!)
print(arr4.dtype)          # → <U21

# ⚠️ AI/ML importance:
# This is why you always check dtype before feeding data to ML model!
# Model expects float32 but you accidentally have strings → model breaks!






# ===== 4. NUMPY ARRAY OPERATIONS =====
heights = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
weights = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

# Element-wise operations (applies to EACH element!)
print(heights * 100)       # convert to cm
print(weights / 2.205)     # convert to pounds

# BMI calculation (element-wise!)
bmi = weights / heights ** 2
print(bmi)                 # → [21.85, 20.97, 21.75, 24.75, 21.44]

# ⚠️ This would be impossible with lists!
# With lists you'd need a loop - with NumPy one line!








# ===== 5. SUBSETTING NUMPY ARRAYS =====
bmi = np.array([21.85, 20.97, 21.75, 24.75, 21.44])

# Normal indexing (same as lists)
print(bmi[0])              # → 21.85
print(bmi[-1])             # → 21.44
print(bmi[1:3])            # → [20.97, 21.75]

# Boolean indexing ⚠️ NEW & CRITICAL FOR AI/ML!
print(bmi > 22)            # → [False False False True False]
print(bmi[bmi > 22])       # → [24.75] (only values where True!)

# ⚠️ AI/ML importance:
# This is how you FILTER data in ML pipelines!
# "Give me all samples where accuracy > 0.9"
# accuracies[accuracies > 0.9]









# ===== 6. 2D NUMPY ARRAYS =====
# Like a matrix - rows and columns

np_2d = np.array([[1.73, 65.4],
                   [1.68, 59.2],
                   [1.71, 63.6],
                   [1.89, 88.4],
                   [1.79, 68.7]])

print(np_2d.shape)         # → (5, 2) = 5 rows, 2 columns
print(np_2d.dtype)         # → float64







# ===== 7. SUBSETTING 2D ARRAYS =====
# np_2d[row, col]  OR  np_2d[row][col]

print(np_2d[0])            # → entire first row
print(np_2d[0][0])         # → 1.73 (row 0, col 0)
print(np_2d[0, 0])         # → 1.73 (same thing, cleaner!)

# Slicing rows and columns
print(np_2d[:, 0])         # → ALL rows, col 0 (all heights!)
print(np_2d[:, 1])         # → ALL rows, col 1 (all weights!)
print(np_2d[1, :])         # → row 1, ALL columns
print(np_2d[0:2, 0:2])     # → first 2 rows, first 2 cols

# ⚠️ AI/ML importance:
# Dataset = 2D array (rows=samples, cols=features)
# X[:, 0] → get first feature for ALL samples
# X[0, :] → get ALL features for first sample
# This notation is used EVERYWHERE in ML!







# ===== 8. 2D ARITHMETIC =====
import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])

print(np_mat * 2)          # multiply every element by 2
print(np_mat + np_mat)     # add matrices element-wise
print(np_mat ** 2)         # square every element








# ===== 9. NUMPY STATISTICS =====
import numpy as np
heights = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
weights = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

# Basic stats
print(np.mean(heights))    # → average
print(np.median(heights))  # → middle value
print(np.std(heights))     # → standard deviation
print(np.min(heights))     # → minimum
print(np.max(heights))     # → maximum
print(np.sum(heights))     # → total sum

# Correlation
print(np.corrcoef(heights, weights))  # → 2x2 correlation matrix

# ⚠️ mean vs median - CRITICAL FOR AI/ML:
data = np.array([1, 2, 3, 4, 100])  # 100 is outlier!
print(np.mean(data))       # → 22.0  (affected by outlier!)
print(np.median(data))     # → 3.0   (NOT affected by outlier!)
# In ML: always check both! If mean >> median → outliers present!










# ===== 10. SHAPE AND DTYPE - ALWAYS CHECK THESE! =====
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr.shape)           # → (2, 3) = 2 rows, 3 cols
print(arr.dtype)           # → int64
print(arr.size)            # → 6 (total elements)
print(arr.ndim)            # → 2 (number of dimensions)

# ⚠️ In ML debugging - first thing you always check:
# print(X.shape)  → make sure data has right dimensions
# print(X.dtype)  → make sure data is float not string







# ===== KEY TAKEAWAYS FOR AI/ML =====
# 1. NumPy arrays = single datatype only (check dtype!)
# 2. Element-wise operations = no loops needed (fast!)
# 3. Boolean indexing = filter data with conditions
# 4. 2D array subsetting: arr[row, col], arr[:, col], arr[row, :]
# 5. mean vs median - always compare to detect outliers
# 6. Always check .shape and .dtype when debugging ML code
# 7. corrcoef - check feature correlations before building model





# 1. np.zeros, np.ones, np.arange (used constantly!)
np.zeros((3, 3))           # 3x3 matrix of zeros
np.ones((2, 4))            # 2x4 matrix of ones
np.arange(0, 10, 2)        # → [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)       # → [0, 0.25, 0.5, 0.75, 1.0]

# 2. reshape (used everywhere in deep learning!)
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.reshape(2, 3))   # → 2 rows, 3 cols
print(arr.reshape(3, 2))   # → 3 rows, 2 cols
# Images in CNN: reshape(28, 28) for MNIST!

# 3. np.random (used for initializing ML models!)
np.random.seed(42)              # for reproducibility!
np.random.rand(3, 3)            # random floats 0-1
np.random.randint(0, 10, (3,3)) # random ints









# coming later

# 1. Broadcasting (very important!)
arr = np.array([[1,2,3],[4,5,6]])
arr + 10        # adds 10 to EVERY element
arr + np.array([1,2,3])  # adds row-wise

# 2. np.where (used constantly in ML!)
arr = np.array([1, -2, 3, -4, 5])
np.where(arr > 0, arr, 0)  # → [1, 0, 3, 0, 5]
# replace negatives with 0 - used in ReLU activation function!

# 3. Stacking arrays
np.vstack([arr1, arr2])   # vertical stack (add rows)
np.hstack([arr1, arr2])   # horizontal stack (add cols)

# 4. np.concatenate
np.concatenate([arr1, arr2], axis=0)  # same as vstack

# 5. Axis parameter (confuses everyone!)
arr = np.array([[1,2,3],
                [4,5,6]])
np.sum(arr)          # → 21 (sum everything)
np.sum(arr, axis=0)  # → [5,7,9] (sum each COLUMN)
np.sum(arr, axis=1)  # → [6,15]  (sum each ROW)
# axis=0 = down (rows), axis=1 = across (columns)

# 6. np.sort
arr = np.array([3,1,4,1,5,9])
np.sort(arr)          # → [1,1,3,4,5,9]
np.argsort(arr)       # → indices that would sort array
                      # used to rank predictions in ML!

# 7. np.unique
arr = np.array([1,2,2,3,3,3])
np.unique(arr)        # → [1,2,3] unique values
                      # used to find unique classes in dataset!

# 8. Saving and loading arrays
np.save('array.npy', arr)      # save
arr = np.load('array.npy')     # load
# used for saving preprocessed datasets!

# 9. np.dot (matrix multiplication - HEART of neural networks!)
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
np.dot(A, B)          # matrix multiplication
# Every neural network layer = np.dot(weights, inputs)!

# 10. np.clip
arr = np.array([-1, 0.5, 2, 3])
np.clip(arr, 0, 1)    # → [0, 0.5, 1, 1]
# clips values between min and max
# used in normalizing pixel values (0 to 1)





#   Most important ones to remember for internship interviews:

# reshape()       Images fed to CNN need specific shape
# np.dot()        Heart of neural networks
# axis=0/1        Every interviewer asks this!
# np.where()      ReLU activation function uses this
# boolean indexing           Filtering dataset samples
# np.random.seed(42)         Reproducibility — every ML script needs this
# mean vs median             Detecting outliers in data