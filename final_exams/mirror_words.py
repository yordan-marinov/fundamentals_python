import re

string = input()

regex = r"(#|@)([a-zA-Z]{3,})\1{2}([a-zA-Z]{3,})\1"

matched = re.finditer(regex, string)
matched_list = [pair.group() for pair in re.finditer(regex, string)]

if not matched_list:
    print("No word pairs found!")
else:
    print(f"{len(matched_list)} word pairs found!")

mirror_words = [
    " <=> ".join([match.group(2), match.group(3)])
    for match in matched
    if match.group(2) == match.group(3)[::-1]
]

if mirror_words:
    print("The mirror words are:")
    print(*mirror_words, sep=", ")
else:
    print("No mirror words!")
