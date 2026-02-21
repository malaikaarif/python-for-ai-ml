# Lecture 09: Regular Expressions in Python
# Topics covered:
# 1. re.search()  -> find first match
# 2. re.findall() -> find all matches
# 3. re.split()   -> split text using pattern
# 4. re.sub()     -> replace pattern in text


# Import regex module
import re


# Sample text
text = "The rain in Spain falls mainly in the plain."

print("Original Text:")
print(text)


# -----------------------------------------
# Search for first occurrence

match = re.search(r"rain", text)

if match:
    print(f"\nMatch found: {match.group()}")
    print(f"Position: {match.start()} to {match.end()}")


# -----------------------------------------
# Find all matches

all_matches = re.findall(r"ain", text)
print(f"\nAll matches of 'ain': {all_matches}")


# -----------------------------------------
# Split text using space

split_text = re.split(r"\s", text)
print(f"\nSplit text into words:")
print(split_text)


# -----------------------------------------
# Replace text using regex

replaced_text = re.sub(r"ain", "XYZ", text)
print(f"\nReplaced text:")
print(replaced_text)
