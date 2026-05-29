# Lecture 06: Exception Handling in Python
# Topics covered:
# 1. try and except blocks
# 2. Handling multiple exceptions
# 3. else block
# 4. finally block
# 5. File handling with exception handling


# -----------------------------------------
# Example 1: Handling arithmetic exceptions

try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))

    result = num1 / num2
    print(f"The result is {result}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input. Please enter integers only.")






# -----------------------------------------
# Example 2: Handling file-related exceptions

try:
    with open("example.txt", "r") as file:
        content = file.read()
        print("File Content:")
        print(content)

except FileNotFoundError:
    print("Error: The file does not exist.")

else:
    print("File read successfully!")

finally:
    print("Operation complete.")
