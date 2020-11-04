def indexes_validated(lst, i, ii):
    return (
            (i != ii) and
            (i in range(len(lst)) and ii in range(len(lst)))
    )


def adding_elements(lst, moves, twins):
    print(
        "Invalid input! "
        "Adding additional elements to the board"
    )

    middle = len(lst) // 2

    return (
            lst[:middle] +
            [f"-{moves}a" for _ in range(twins)] +
            lst[middle:]
    )


def valid_indexes(lst, i, ii):
    if lst[i] == lst[ii]:
        popped_element = lst.pop(i)
        lst.remove(popped_element)
        print(
            f"Congrats! "
            f"You have found matching elements - "
            f"{popped_element}!"
        )
    else:
        print("Try again!")

    return lst


sequence = input().split()

TWINS = 2

moves = 0
while True:

    data = input()
    if data == "end":
        print(f"Sorry you lose :(")
        print(*sequence)
        break

    moves += 1

    index_1, index_2 = [int(i) for i in data.split()]

    if not indexes_validated(sequence, index_1, index_2):
        sequence = adding_elements(sequence, moves, TWINS)
        continue

    valid_indexes(sequence, index_1, index_2)

    if not sequence:
        print(f"You have won in {moves} turns!")
        break
