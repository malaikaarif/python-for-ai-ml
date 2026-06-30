# ============================================
# DataCamp - Chapter 2 - PRACTICE
# ============================================

# ===== LEVEL 1: BASICS =====

# Q1. Create a list called `student` with:
# your name, age, GPA, is_enrolled(True/False)
# Print the whole list and its type



student = ["Malaika Arif", 22, 3.60, True]
print(student)
print(type(student))






# Q2. Predict the output WITHOUT running:
nums = [10, 20, 30, 40, 50]
print(nums[0])        # 10
print(nums[-1])       # 50
print(nums[1:3])      # 20,30
print(nums[:2])       # 10,20
print(nums[3:])       # 40,50

# Slicing always returns a list, even with single elements:





# ===== LEVEL 2: INDEXING & SLICING =====

# Q3. Given this list:
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
# Get these using NEGATIVE indexing only:
# 1. last element       fam[-1]
# 2. "mom"              fam[-4]
# 3. first 3 elements using negative slicing      fam[:-5]






# Q4. Predict WITHOUT running:
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
print(fam[2:])                        # ["emma", 1.68, "mom", 1.71, "dad", 1.89]
print(fam[:-4])                       # ["liz", 1.73. "emma", 1.68]
print(fam[::2])   # ← new! figure this one out 🤔           ["liz", "emma","mom","dad"]






# ===== LEVEL 3: LIST OF LISTS =====

# Q5. Create a 2D list called `classroom`:
# 3 students, each with [name, grade, score]
# Access:
# 1. second student's name
# 2. third student's score
# 3. entire second row


classroom = [["Malaika", "A+",3.60],
             ["Iqra","A+", 3.63],
             ["Aleena","A+",3.62]
             ]
print(classroom[1][0])
print(classroom[2][2])
print(classroom[1])

# This is exactly how you'd access rows/columns in a real dataset!






# Q6. Predict the output:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[0][2])              # 3
print(matrix[1][1])              # 5
print(matrix[2][0])              # 7
print(matrix[-1][-1])            # 9

# This matrix[-1][-1] trick is used constantly to get the bottom-right corner of any 2D grid/image in AI/ML!





# ===== LEVEL 4: MANIPULATING =====

# Q7. Start with this list:
scores = [75, 82, 91, 68, 95]
# 1. Replace 68 with 88
# 2. Add [100, 79] to the end
# 3. Delete the first element
# 4. Print final list

scores[3]=88
print(scores)

scores = scores + [100,79]
print(scores)

del scores[0]
print(scores)









# Q8. What's the bug and fix it:
original = [1, 2, 3, 4, 5]
backup = original
backup[0] = 999
print(original)   # should print [1, 2, 3, 4, 5] but doesn't!
# Fix the code!



original = [1, 2, 3, 4, 5]
backup = list(original)             # creates actual copy
backup[0]=999
print(original)



# This is the exact bug that breaks real ML pipelines — people accidentally modify their original training data while trying to create a "backup" or "test copy"! 














# ===== LEVEL 5: AI/ML CHALLENGE =====

# Q9. You have a dataset of 10 student scores:
scores = [45, 67, 89, 34, 78, 92, 55, 71, 88, 63]

# 1. Get first 5 scores (training set)       
print(scores[:5])
# 2. Get last 5 scores (test set)
print(scores[-5:])
# 3. Get every other score using slicing
print(scores[::2])
# 4. Replace score at index 3 (34) with 74
scores[3] = 74
print(scores)
# 5. Print: "Highest possible index is X" 
#    (without hardcoding the number!)

print("Highest possible index is: ",len(scores)-1)









# Q10. 2D Dataset challenge:
dataset = [
    ["Alice", 25, 85.5],
    ["Bob", 30, 92.0],
    ["Sara", 22, 78.3],
    ["John", 28, 95.1]
]

# 1. Get Alice's score
print(dataset[0][2])

# 2. Get all of Bob's data
print(dataset[1])
# 3. Get only the first 2 students
print(dataset[0:2])
# 4. Change Sara's score to 88.0
dataset [2][2] = 88.0
print(dataset)  
# 5. Add new student ["Malaika", 21, 98.0]
dataset = dataset + [["Malaika", 21, 98.0]]

# 6. Print the final dataset
print(dataset)

# Key lesson: When adding a new "row" to a 2D list, you must add a list containing
# a list, not just raw values! This is a classic bug in real data preprocessing. 💡