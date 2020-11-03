list_of_numbers = input().split()
massage = input()

element_index = []
for number in list_of_numbers:
    num = 0
    for character in number:
        num += int(character)
    element_index.append(num)


character_massage = [c for c in massage]


new_message = ""
for element in element_index:
    index = 0
    while index != element:

        for item in character_massage:
            if index == element:
                new_message += item
                character_massage.remove(item)
                break

            index += 1


print(new_message)
