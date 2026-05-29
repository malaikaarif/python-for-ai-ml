# Lecture 04: File Handling in Python
# Repository: python-for-ai-ml
# Author: Malaika Arif
# Description: Demonstrates write, read, append, and delete file operations.




# -------------------------------------------
# WRITE MODE
# "w" mode creates a new file or overwrites existing file


file = open("example.txt","w")
file.write("Hello, this is a test file.\n")
file.write("Python file handling is fun!")

file.close()               # Always close the file after writing

print("File created and data written successfully!")







# -------------------------------------------
# READ MODE
# "r" mode reads the content of the file


file = open("example.txt","r")
content=file.read()
print("File content")
print(content)

file.close()          # Close after reading










# -------------------------------------------
# APPEND MODE
# "a" mode adds new content without deleting old content
file=open("example.txt","a")

file.write("\nThis line was added using append mode")

file.close()

print("Data appended to file successfully!")


# Read again to verify appended content
file = open("example.txt","r")
content=file.read()
print("File content")
print(content)

file.close()



# -------------------------------------------
# DELETE FILE
# os module is used to perform file operations like delete

import os
os.remove("example.txt")

print("File deleted successfully!")

