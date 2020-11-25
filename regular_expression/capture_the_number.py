import re

text = input()
numbers = []
while len(text) > 0:

    regex = r"\d+"
    current_numbers = re.finditer(regex, text)

    for current_number in current_numbers:
        numbers.append(current_number.group(0))

    text = input()


print(*numbers)