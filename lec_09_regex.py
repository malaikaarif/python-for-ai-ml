import re

text = "The rain is Spain falls mainly in the plain."

match = re.search(r"rain", text)

if match:
    print(f"Match found: {match.group()} at position {match.start()}-{match.end()}")

all_matches = re.findall(r"ain",text)    

print(f"All matches: {all_matches}")

split_text = re.split(r"\s", text)
print(f"Split text: {split_text}")

replaced_text = re.sub(r"ain","XYZ",text)
print(f"Replaced text: {replaced_text}")