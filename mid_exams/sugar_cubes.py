def adding_element(lst, value):
    lst.append(value)

    return lst


def remove_element(lst, value):
    if value in lst:
     lst.remove(value)

    return lst


def replace_element(lst, value, new_value):
    if value in lst:
        lst[lst.index(value)] = new_value

    return lst


def collapse(lst, value):
    value = int(value)
    lst = [e for e in lst if int(e) >= value]

    return lst


sugar_cubes = input().split()

while True:

    data = input()
    if data == "Mort":
        print(*sugar_cubes)
        break

    command, *token = data.split()

    if command == "Add":
        sugar_cubes = adding_element(sugar_cubes, *token)

    elif command == "Remove":
        sugar_cubes = remove_element(sugar_cubes, *token)

    elif command == "Replace":
        sugar_cubes = replace_element(sugar_cubes, *token)

    elif command == "Collapse":
        sugar_cubes = collapse(sugar_cubes, *token)
