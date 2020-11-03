def delete(lst, e):
    while e in lst:
        lst.remove(e)
    return lst


def insert_number(lst, e, i):
    lst.insert(i, e)
    return lst


def odd(lst):
    return [n for n in lst if n % 2 != 0]


def even(lst):
    return [n for n in lst if n % 2 == 0]


numbers = [int(n) for n in input().split()]

while True:
    command = input()
    if command == "Odd" or command == "Even":
        break

    token = command.split()
    cmd_name = token[0]
    element = int(token[1])

    if cmd_name == "Delete":
        numbers = delete(numbers, element)

    elif cmd_name == "Insert":
        position = int(token[2])
        numbers = insert_number(numbers, element, position)


if command == "Odd":
    print(" ".join([str(i) for i in odd(numbers)]))
elif command == "Even":
    print(" ".join([str(i) for i in even(numbers)]))
