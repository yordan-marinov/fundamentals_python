import re

data = input()
regex = r"\+359([\s-])2\1[0-9]{3}\1[0-9]{4}\b"

matches = re.finditer(regex, data)

print(', '.join([i.group() for i in matches]))
