def change(lst, old_num, new_num):
    if old_num in lst:
        lst[lst.index(old_num)] = new_num

    return lst


def hide_num(lst, num):
    if num in lst:
        lst.remove(num)

    return lst


def switch(lst, number_1, number_2):
    if number_1 in lst and number_2 in lst:
        i_1, i_2 = lst.index(number_1), lst.index(number_2)
        lst[i_1], lst[i_2] = lst[i_2], lst[i_1]

    return lst


def insert_num(lst, i, num):
    if i in range(len(lst)):
        lst.insert(i + 1, num)

    return lst


paintings = input().split()

while True:

    data = input()
    if data == "END":
        print(*paintings)
        break

    token = data.split()
    command = token[0]

    if command == "Change":
        old_number = token[1]
        new_number = token[2]
        paintings = change(paintings, old_number, new_number)

    elif command == "Hide":
        number = token[1]
        paintings = hide_num(paintings, number)

    elif command == "Switch":
        num_1 = token[1]
        num_2 = token[2]
        paintings = switch(paintings, num_1, num_2)

    elif command == "Insert":
        index = int(token[1])
        number = token[2]
        paintings = insert_num(paintings, index, number)

    elif command == "Reverse":
        paintings = paintings[::-1]
