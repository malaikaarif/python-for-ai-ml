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
print(students["passed"]==True)