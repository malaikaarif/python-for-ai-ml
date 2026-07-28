# ============================================
# Chapter 3: Logic, Control Flow & Filtering
# PRACTICE QUESTIONS
# ============================================

# ===== LEVEL 1: Comparison & Boolean Operators =====

# Q1. Predict the output WITHOUT running:
x = 7
y = 12
print(x > 5 and y < 10)    # false
print(x > 5 or y < 10)     # True
print(not x > 5)           # false










# Q2. You have:
import numpy as np
temps = np.array([30, 45, 22, 38, 50])
# Write a line that gives a boolean array of which temps are above 35.

print(temps > 35)







# Q3. Fix this broken code (it will throw an error) and explain why it breaks:
import numpy as np
a = np.array([10, 20, 30])
b = np.array([15, 25, 35])
# result = a > 15 and b > 20

print(np.logical_and(a>15,b>20))







# ===== LEVEL 2: if / elif / else =====

# Q4. Write an if/elif/else block: given a variable `marks`,
# print "A" if marks >= 90, "B" if marks >= 75, "C" if marks >= 50,
# else print "Fail".

marks=50
if marks >= 90:
    print ("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")        
else:
    print("Fail")











# Q5. Predict the output WITHOUT running:
z = 20
if z > 10:
    print("Big")
elif z > 5:
    print("Medium")
else:
    print("Small")
# Why does it only print ONE of these, even though z > 5 is also true?


# in first cond, it will check z > 10 - in second z > 5 - both conditions r correct but first cond is closer to value
# that's why but the sec cond is farrrr


# it's about order and stopping on the first True. Python reads top to bottom:


# Checks z > 10 → 20 > 10 → True → prints "Big" and immediately stops checking anything below it.
# It never even looks at z > 5, even though that's also technically True. Once one condition matches, Python skips
#  the rest of the chain entirely — no exceptions.



# first True condition wins, and everything after is ignored."














# Q6. Write a one-line ternary expression: given `speed`, 
# assign result = "fast" if speed > 60 else "slow"


speed=70
result="fast" if speed > 60 else "slow"









# ===== LEVEL 3: DataFrame Filtering =====
# Use this DataFrame for Q7-Q11:
import pandas as pd
students = pd.DataFrame({
    "name": ["Ali", "Sara", "Zain", "Hina", "Omar"],
    "attendance": [85, 60, 92, 70, 45],
    "grade": [78, 55, 88, 65, 40],
    "passed": [True, False, True, True, False]
})





# Q7. Filter students where attendance is greater than 70.
print(students[students["attendance"]>70])




# Q8. Filter students where passed == True (two different ways —
#     one using == True explicitly, one using the column directly).
print(students[students["passed"]==True])
print(students[students["passed"]])



# Q9. Filter students where BOTH attendance > 65 AND grade > 60
#     using np.logical_and().

print(students[np.logical_and(students["attendance"]>65,students["grade"]>60)])





# Q10. Now write the SAME filter as Q9 but using pandas & syntax
#      instead of np.logical_and().

print(students[(students["attendance"]>65) & (students["grade"]>65)])



# Q11. Use .isin() to filter students whose name is either "Ali" or "Omar".

print(students[students["name"] .isin(["Ali","Omar"])])


# ===== LEVEL 4: Bonus / Real-World Shortcuts =====

# Q12. You have: 
results = np.array([0.65, 0.82, 0.91, 0.55, 0.78])
# Using .any() and .all(), answer:
# a) Is at least one result above 0.9?                     .any()
print((results > 0.9).any())
# b) Are ALL results above 0.5?     #                        .all()
print((results>0.5).all())




# Q13. Use .between() to filter `students` for attendance between 60 and 90.
print(students[students["attendance"] .between(60,90)])



# Q14. Rewrite Q9's filter using df.query() instead.
print(students.query("attendance>65 and grade>60"))