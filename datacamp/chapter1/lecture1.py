# ============================================
# DataCamp - Introduction to Python
# Chapter 1 - Python Basics - COMPLETE NOTES
# ============================================

# ===== 1. PYTHON AS A CALCULATOR =====
print(4 + 5)     # addition       → 9
print(10 / 2)    # division       → 5.0 (ALWAYS float) *******
print(10 // 2)   # floor division → 5   (INT, removes decimal)
print(10 % 3)    # modulo         → 1   (remainder)
print(3 * 5)     # multiplication → 15
print(2 ** 3)    # exponentiation → 8   (2 to the power 3)

# ⚠️ IMPORTANT FOR AI/ML:
# / always returns float even if result is whole number
print(10 / 2)    # → 5.0 NOT 5
# // floors the result (rounds DOWN always)
print(int(-3.5))   # → -3  (toward zero)
print(-7 // 2)   # → -4 NOT -3 (floors toward negative infinity)





# ===== 2. VARIABLES =====
# Variable = a name that stores a value in memory
x = 5            # int
y = 2.5          # float
name = "Malaika" # string
is_student = True # boolean

# Rules for variable names:
# ✅ can use letters, numbers, underscore
# ✅ monthly_savings, x1, my_var
# ❌ cannot start with number → 1var (wrong)
# ❌ cannot use spaces → my var (wrong)
# ❌ case sensitive → Name and name are DIFFERENT variables







# ===== 3. DATA TYPES =====
print(type(5))        # <class 'int'>
print(type(2.5))      # <class 'float'>
print(type("hello"))  # <class 'str'>
print(type(True))     # <class 'bool'>






# ===== 4. TYPE CONVERSION (not in DataCamp but CRITICAL) =====
# Converting between types
print(int(2.9))      # → 2   (truncates, does NOT round)
print(float(5))      # → 5.0
print(str(100))      # → "100"
print(bool(0))       # → False
print(bool(1))       # → True
print(bool(""))      # → False (empty string is False)
print(bool("hello")) # → True  (any non-empty string is True)





# ===== 5. BOOLEAN TRICKS (critical for AI/ML) =====
print(True + True)        # → 2  (True = 1, False = 0)
print(True + False)       # → 1
print(False * 5)          # → 0
print(True + True + False * 5)  # → 2





# ===== 6. FLOATING POINT TRAP ⚠️ =====
# This is a famous bug that breaks ML models!
x = 0.1 + 0.2
print(x)          # → 0.30000000000000004 (NOT 0.3!)
print(x == 0.3)   # → False !!!

# Why? Computers store floats in binary
# 0.1 cannot be represented exactly in binary

# Fix in ML code:
print(round(x, 1) == 0.3)  # → True
# OR use numpy (you'll learn this in Chapter 4)
# np.isclose(0.1 + 0.2, 0.3) → True




# ===== 7. STRING OPERATIONS =====
first = "Python"
last = "rocks"
print(first + " " + last)  # → "Python rocks" (concatenation)
print(first * 3)            # → "PythonPythonPython" (repetition)





# ===== 8. OPERATIONS WITH DIFFERENT TYPES =====
# ❌ Cannot mix str and int
# print("Age: " + 25)  → TypeError!

# ✅ Convert first
age = 25
print("Age: " + str(age))   # → "Age: 25"

# ===== KEY TAKEAWAYS FOR AI/ML =====
# 1. / always gives float - important when working with arrays
# 2. Floating point is never exact - never use == with floats in ML
# 3. bool is subclass of int - True=1, False=0 (used in masking)
# 4. Type errors are common bugs - always check types when debugging ******


mem_mb = 100    # assume only
# You used this in Q8 but don't have it in notes
print(f"Value is {mem_mb:.2f}")   # :.2f = 2 decimal places
print(f"Value is {mem_mb:.4f}")   # :.4f = 4 decimal places
print(f"Value is {mem_mb:.0f}")   # :.0f = whole number

# Also useful in ML:
epoch = 5
loss = 0.324567
print(f"Epoch {epoch}: loss = {loss:.4f}")  # → Epoch 5: loss = 0.3246