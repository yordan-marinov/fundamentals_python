import re

data = input()

regex = r"(^|(?<=\s))-?\d*\.?\d+($|(?=\s))"

numbers = re.finditer(regex, data)

[
    print(number.group(), end=" ")
    for number in numbers
]
