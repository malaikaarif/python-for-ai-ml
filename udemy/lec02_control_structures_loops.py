# Lecture 02: Control Structures and Loops
# Repository: python-for-ai-ml
# Author: Malaika Arif
# Description: Demonstrates if-elif-else statements, for loop, and while loop in Python.

# ---------------------------------------
# Conditional Statements (if-elif-else)
# ---------------------------------------

number = int(input("Enter a number:"))

if number>0:
    print("The number is positive")
elif number<0:
    print("The number is negative")
else:
    print("The number is zero")        




# ---------------------------------------
# For Loop Example
# ---------------------------------------


print("\nFor loop from 1 to 5:")
for i in range(1,6):
    print(i)  





# ---------------------------------------
# While Loop Example
# ---------------------------------------


print("\nCountdown using while loop:")
count=5
while count>0:
    print(count)
    count-=1             # decrease count by 1


print("Blast off!")        