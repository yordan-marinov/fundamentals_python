import re

regex = r"\b(_)([a-zA-Z0-9]+)\b"

text = input()

matched_variables = re.finditer(regex, text)

print(
    ','.join(
[
    matched.group(2)
    for matched in matched_variables
]
    )
)
