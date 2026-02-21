# Lecture 05: Object-Oriented Programming (OOP) in Python
# Topics covered:
# 1. Classes and Objects
# 2. Constructors (__init__)
# 3. Methods
# 4. Inheritance
# 5. Method overriding


# -----------------------------------------
# Example 1: Creating a Class and Object

class Person:
    # Constructor method (automatically called when object is created)
    def __init__(self, name, age):
        self.name = name    # instance variable
        self.age = age      # instance variable

    # Method to display greeting
    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

    # Method to increase age
    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")


# Creating object of Person class
person1 = Person("Malaika", 21)

# Calling methods
print(person1.greet())
person1.have_birthday()







# -----------------------------------------
# Example 2: Inheritance

# Parent class (Base class)
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some generic animal sound"


# Child class (Derived class)
class Dog(Animal):

    # Method overriding
    def sound(self):
        return "Woof! Woof!"


# Creating objects
generic_animal = Animal("Generic Animal")
dog = Dog("Buddy")

# Calling methods
print(generic_animal.sound())   # Parent class method
print(dog.sound())              # Child class overridden method
