import re

line = input()

regex = r"w{3}\.[a-zA-Z0-9-]+\.[a-z]+(\.[a-z]+)*"

while len(line) > 0:

    matched = re.finditer(regex, line)
    for match in matched:
        print(match.group())

    line = input()