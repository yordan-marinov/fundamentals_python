from collections import defaultdict
import re

racers = {racer: 0 for racer in input().split(", ")}

while True:

    data = input()
    if data == "end of race":
        break

    regex = r"[A-Za-z0-9]"

    racers_info = re.findall(regex, data)

    name = "".join([letter for letter in racers_info if letter.isalpha()])
    distances = sum([int(digit) for digit in racers_info if digit.isdigit()])

    if name in racers:
        racers[name] += distances

racers = sorted(racers.items(), key=lambda a: (-a[1]))
end = None
for index, name in enumerate(racers, 1):
    if index == 1:
        print(f"{index}st place: {name[0]}")
    if index == 2:
        print(f"{index}nd place: {name[0]}")
    if index == 3:
        print(f"{index}rd place: {name[0]}")
        break

