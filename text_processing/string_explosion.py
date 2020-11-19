line = input()

result = ""
power = 0
for index, element in enumerate(line):
    if power:
        if element == ">":
            result += element
            power += int(line[index + 1])
            continue
        power -= 1
    else:
        result += element

        if element == ">":
            power += int(line[index + 1])

print(result)
