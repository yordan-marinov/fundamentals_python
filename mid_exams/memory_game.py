def matching_elements_manipulator(lst, first_index, second_index):
    if lst[first_index] == lst[second_index]:
        removed_element = lst.pop(first_index)
        lst.remove(removed_element)
        print(
            f"Congrats! You have found matching elements - {removed_element}!"
        )

    else:
        print("Try again!")
    return lst


def split_elements(lst, count):
    middle = len(lst) // 2
    lst = (
            lst[:middle] +
            [f"-{count}a" for _ in range(2)] +
            lst[middle:]
    )
    print("Invalid input! Adding additional elements to the board")
    return lst


def indexes_validation(lst, first_index, second_index):
    return (
            (first_index == second_index) or
            (first_index not in range(len(lst))) or
            (second_index not in range(len(lst)))
    )


sequence = input().split()

number_of_moves = 0
flag = False

while True:
    command = input()
    if command == "end":
        break

    number_of_moves += 1

    token = command.split()
    index_1 = int(token[0])
    index_2 = int(token[1])

    if indexes_validation(sequence, index_1, index_2):
        sequence = split_elements(sequence, number_of_moves)

    else:
        sequence = matching_elements_manipulator(sequence, index_1, index_2)

    if not sequence:
        print(f"You have won in {number_of_moves} turns!")
        flag = True
        break

if not flag:
    print("Sorry you lose :(")
    print(" ".join(sequence))
