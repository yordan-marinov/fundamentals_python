import re

regex = r"^(\$|\%)([A-Z][a-z]{2,})\1:\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"

count = int(input())

for _ in range(count):
    string = input()
    matched = re.findall(regex, string)

    if not matched:
        print("Valid message not found!")
    else:
        word = chr(int(matched[0][2]))+chr(int(matched[0][3]))+chr(int(matched[0][4]))
        print(f"{matched[0][1]}: {word}")
