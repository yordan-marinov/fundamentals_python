line = input()

result = ""
current_element = ""
digit_str = ""
for index, element in enumerate(line):
    if element.isdigit():
        digit_str += element
        if index != len(line) - 1:
            continue
    if digit_str:
        result += current_element.upper() * int(digit_str)
        current_element = ""
        digit_str = ""

    current_element += element


print(f'Unique symbols used: {len(set(result))}')
print(result)
