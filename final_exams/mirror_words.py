import re

regex = r"(@|#)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"

string = input()

matched = re.findall(regex, string)
if not matched:
    print("No word pairs found!")
else:
    print(f"{len(matched)} word pairs found!")

mirror_words = [
    ' <=> '.join([word.group(2), word.group(3)])
    for word in re.finditer(regex, string)
    if word.group(2) == word.group(3)[::-1]
]
if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(*mirror_words, sep=", ")
