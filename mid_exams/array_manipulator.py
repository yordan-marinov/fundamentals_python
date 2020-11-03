from itertools import zip_longest


def adding(lst, indx, el):
    lst.insert(indx, el)
    return lst


def adding_many(lst, indx, lst_1):
    lst[indx:indx] = lst_1
    return lst


def contains_element(lst, el):
    if el in lst:
        print(lst.index(el))
    else:
        print(-1)


def remove_element(lst, indx):
    lst.pop(indx)
    return lst


def shifting(lst):
    return lst.append(lst.pop(0))


def sum_pairs(lst):
    l_1 = [lst[i] for i in range(len(lst)) if i % 2 != 0]
    l_2 = [lst[i] for i in range(len(lst)) if i % 2 == 0]
    return [i + j for i, j in zip_longest(l_1, l_2, fillvalue=0)]


numbers = [int(i) for i in input().split()]


while True:

    data = input().split()
    command = data.pop(0)

    if command == "add":
        index, element = int(data[0]), int(data[1])
        numbers = adding(numbers, index, element)

    elif command == "addMany":
        index = int(data[0])
        elements = [int(i) for i in data[1:]]
        numbers = adding_many(numbers, index, elements)
        del elements

    elif command == "contains":
        element = int(*data)
        contains_element(numbers, element)

    elif command == "remove":
        index = int(*data)
        numbers = remove_element(numbers, index)

    elif command == "shift":
        positions_count = int(*data)
        [shifting(numbers) for _ in range(positions_count)]

    elif command == "sumPairs":
        numbers = sum_pairs(numbers)

    elif command == "print":
        print(numbers)
        break
