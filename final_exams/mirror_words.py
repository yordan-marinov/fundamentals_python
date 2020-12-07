import re

regex = r"(#|@)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})"

text_string = input()

matched = re.findall(regex, text_string)

if not matched:
    print("No word pairs found!")
else:
    print(f"{len(matched)} word pairs found!")

mirror_words = []
for match in matched:
    if match[1] == match[2][::-1]:
        mirror_words.append(" <=> ".join(match[1:]))

if mirror_words:
    print("The mirror words are:")
    print(*mirror_words, sep=", ")
else:
    print("No mirror words!")
