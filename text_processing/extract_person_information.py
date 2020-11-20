def splitter(string, splitter_1, splitter_2):
    first = string.split(splitter_1)
    second = first[1].split(splitter_2)
    return second[0]


number_lines = int(input())

for _ in range(number_lines):
    line = input()

    name = splitter(line, "@", "|")
    age = splitter(line, "#", "*")

    print(f"{name} is {age} years old.")
