def shoot(lst, token):

    items = token.split("@")
    direction = items.pop(0)
    start_index, length = [int(i) for i in items]

    if direction == "Left":
        return (start_index - length) % len(lst)

    return (start_index + length) % len(lst)


def reversing_list(lst):
    return lst[::-1]


targets = [int(x) for x in input().split("|")]


while True:
    data = input()

    if data == "Game over":
        break

    command = data.split()

    if command[0] == "Shoot":
        targets = shoot(targets, command[1])

    else:
        targets = reversing_list(targets)
