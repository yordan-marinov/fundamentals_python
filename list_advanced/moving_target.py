def shooting(lst, inde_x, v_alue):
    inde_x, v_alue = int(inde_x), int(v_alue)
    if 0 <= inde_x < len(lst):
        lst[inde_x] -= v_alue
        if lst[inde_x] <= 0:
            lst.pop(inde_x)
    return lst


def adding(lst, i_ndex, v_alue):
    i_ndex, v_alue = int(i_ndex), int(v_alue)
    if 0 <= i_ndex < len(lst):
        lst.insert(i_ndex, v_alue)
        return lst
    print("Invalid placement!")
    return lst


def strike(lst, i_ndex, v_alue):
    i_ndex, v_alue = int(i_ndex), int(v_alue)
    start = i_ndex - v_alue
    end = i_ndex + v_alue

    if not (start >= 0 and end < len(lst)):
        print("Strike missed!")
        return lst

    return lst[:start] + lst[end + 1:]


targets = [int(i) for i in input().split()]


while True:

    command = input()

    if command == "End":
        print("|".join([str(i) for i in targets]))
        break

    name_command, index, value = command.split()

    if name_command == "Shoot":
        targets = shooting(targets, index, value)

    elif name_command == "Add":
        targets = adding(targets, index, value)

    elif name_command == "Strike":
        targets = strike(targets, index, value)
