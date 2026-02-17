# Lecture 03: Functions and Modules
# Repository: python-for-ai-ml
# Author: Malaika Arif
# Description: Demonstrates defining functions, taking user input, using the math module, 
#              and importing/calling functions from a custom module.






# ---------------------------------------
# Importing Modules
# ---------------------------------------
import math  # Provides access to mathematical functions like sqrt, sin, cos, etc.

# ---------------------------------------
# Function Example: Greet User
# ---------------------------------------
def greet(name):
    """
    Returns a greeting message for the given name.
    """
    return f"Hello, {name}! Welcome to Python"





# Ask user for their name
user_name = input("Enter your name: ")
# Call greet function and display the greeting
print(greet(user_name))



# ---------------------------------------
# Using math Module
# ---------------------------------------
number = 30
# Calculate square root using math.sqrt()
square_root = math.sqrt(number)
print(f"The square root of {number} is {square_root}")




# ---------------------------------------
# Function Example: Add Two Numbers
# ---------------------------------------
def add_numbers(a, b):
    """
    Returns the sum of two numbers a and b.
    """
    return a + b






# ---------------------------------------
# Using a Function from a Custom Module
# ---------------------------------------
from my_package import module1  # Import module1 from my_package

# Call add_numbers function from module1 and store result
result = module1.add_numbers(5, 7)
print(f"The sum of 5 and 7 is {result}")
