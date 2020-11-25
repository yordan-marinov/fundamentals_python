import re

text = input()
searched_word = input()

regex = fr"\b{searched_word}\b"

found = re.findall(regex, text, re.I)

print(len(found))
