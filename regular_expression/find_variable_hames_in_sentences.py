import re

regex = r"\b(_)([a-zA-Z0-9]+)\b"

text = input()

matched_variables = re.finditer(regex, text)

variables = [
    matched.group(2) for matched in matched_variables
]

print(','.join(variables))
