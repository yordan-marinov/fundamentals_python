def shooting(lst, i, v):
    i, v = int(i), int(v)
    if 0 <= i < len(lst):
        lst[i] -= v
        if lst[i] <= 0:
            lst.pop(i)
    return lst


def adding(lst, i, v):
    i, v = int(i), int(v)
    if 0 <= i < len(lst):
        lst.insert_number(i, v)
        return lst
    print("Invalid placement!")
    return lst


def strike(lst, i, v):
    i, v = int(i), int(v)
    start = i - v
    end = i + v

    if not (0 <= start < len(lst) and 0 <= end < len(lst)):
        print("Strike missed!")
        return lst

    removed_targets = lst[start:end + 1]
    lst = [i for i in lst if i not in removed_targets]
    return lst


targets = [int(i) for i in input().split()]

while True:
    command = input()
    if command == "End":
        break

    name_command, index, value = command.split()

    if name_command == "Shoot":
        targets = shooting(targets, index, value)

    elif name_command == "Add":
        targets = adding(targets, index, value)

    elif name_command == "Strike":
        targets = strike(targets, index, value)

print("|".join([str(i) for i in targets]))
