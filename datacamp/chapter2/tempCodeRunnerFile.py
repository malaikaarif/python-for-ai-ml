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