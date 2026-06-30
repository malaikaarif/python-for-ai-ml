# ============================================
# DataCamp - Chapter 1 - PRACTICE
# ============================================

# ===== LEVEL 1: BASICS =====

# Q1. Calculate and print the result of:
# - 17 divided by 3 (normal division)      -- 5.666666666666667      
# - 17 floor divided by 3                  -- 5
# - 17 modulo 3                            -- 2
# What do you notice about the three results?




# Q2. What will these print? Guess first, then run:
print(type(10 / 2))   # int or float?  -- float
print(type(10 // 2))  # int or float?  -- int
print(type(True))     # what class?    -- bool
print(type(2 ** 3))   # int or float?  -- int
 




# ===== LEVEL 2: VARIABLES & TYPES =====

# Q3. Fix the bugs in this code:
# 1name = "Malaika"     --- variable names cannot start with a number  -- name = "Malaika"
# my age = 21           --- space between variable name                  my_age = 21 
# is Student = True     --- space between variable name --- must  be is_Student          is_Student = True 
# print(type(1name))    -- wrong variable name           print(type(name))





# Q4. What is the output?
x = 10
y = 3
print(x % y)          # ?          1
print(x // y)         # ?          3
print(x ** y)         # ?          1000
print(type(x / y))    # ?          float






# ===== LEVEL 3: TYPE CONVERSION =====

# Q5. Predict the output:
print(int(9.9))       # ?        9
print(int(-9.9))      # ?       -9
print(bool(0))        # ?        False
print(bool(-5))       # ?        True
print(bool(""))       # ?        False
print(bool("False"))  # ? careful!    True







# Q6. Fix this code so it works:
name = "Malaika"
age = 21
# print("My name is " + name + " and I am " + age + " years old")
# fix 1 -->  print("My name is " + name + " and I am " + str(age) + " years old")
# fix 2 -->   age = "21"  -- print("My name is " + name + " and I am " + age + " years old")

# Fix 3 → f-string (most used in real code!)
print(f"My name is {name} and I am {age} years old")
# My name is Malaika and I am 21 years old








# ===== LEVEL 4: BOOLEAN TRICKS =====

# Q7. Predict WITHOUT running:
print(True + True + True)     # ?     3
print(False + False)          # ?     0
print(True * 100)             # ?     100
print(False * 100)            # ?     0
print(True + True * 5)        # ? careful with operator precedence!       6









# ===== LEVEL 5: AI/ML CHALLENGE =====

# Q8. MNIST Dataset Memory Calculator
# You have a dataset with 1000 images
# Each image is 28x28 pixels
# Each pixel is a float32 (4 bytes)

total_images = 1000
image_height = 28
image_width = 28
bytes_per_pixel = 4

# Calculate:
# 1. Total pixels in ONE image                       
total_pixels = image_height * image_width  
print(total_pixels)

# 2. Total pixels in the ENTIRE dataset            
total_pixel = total_images * total_pixels
print(total_pixel)

# 3. Total memory in bytes        
tot_mem = total_pixel * bytes_per_pixel
print(tot_mem)

# 4. Total memory in KB (1 KB = 1024 bytes)     
mem_kb = tot_mem / 1024
print(mem_kb)

# 5. Total memory in MB (1 MB = 1024 KB)   
mem_mb = mem_kb / 1024
print(mem_mb)

# 6. Print: "MNIST dataset takes X MB of memory"    
print(f"MNIST dataset takes {mem_mb:.2f} MB of memory.")









# Q9. FLOATING POINT TRAP
# Why does this matter in ML? Write your answer as a comment

# 0.1+0.2 != 0.3 becoz computers store no.s in bianry and 0.1 = 0.0001001010101 (infinite)
x = 0.1 + 0.2
print(x == 0.3)    # what prints and WHY?   -- it will print false beoz sum of 0.1 and 0.2 is 0.300000004

# Fix it using round()

print(round(0.1+0.2,1))

# Fix it using abs() - hint: abs(x - 0.3) < 0.0001
if abs(x-0.3)<0.0001:
    print("Model is good")










# ===== BONUS =====
# Q10. Predict the output of this:
print(True + True + False * 5 - True * 2)    # 0

# from left to right 
# first False * 5
# then True * 2
# then add
# then subtract afer

# 1 + 1 + 0 * 5 - 1 * 2
# 1 + 1 + 0 - 1 * 2
# 1 + 1 + 0 - 2
# 2 - 2
# 0

