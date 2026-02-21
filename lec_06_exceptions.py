# try:
#     num1=int(input("Enter num1: "))
#     num2=int(input("Enter num2: "))

#     result=num1/num2
#     print(f"The result is {result}")

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed")

# except ValueError:
#     print("Invalid Value")   






try:
    with open ("example.txt","r") as file:
        content=file.read()
        print("File Content: ")
        print(content)

except FileNotFoundError:
    print("The file doesn't exist")

else:
    print("File read successfully!")

finally:
    print("Operation complete")    

        
      

