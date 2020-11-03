def delete(lst, i):
    if i + 1 in range(len(lst)):
        lst.pop(i + 1)

    return lst


def swap(lst, string_1, string_2):
    if string_1 in lst and string_2 in lst:
        index_1, index_2 = lst.index(string_1), lst.index(string_2)
        lst[index_1], lst[index_2] = lst[index_2], lst[index_1]

    return lst


def put(lst, string, i):
    if i + 1 in range(len(lst)):
        if i == len(lst)-1:
            lst.append(string)
        else:
            lst.insert(i - 1, string)

    return lst


def sorting(lst):
    return sorted(lst, reverse=True)


def replace(lst, string_1, string_2):
    if string_2 in lst:
        lst[lst.index(string_2)] = string_1

    return lst


strings = input().split()

while True:

    data = input()
    if data == "Stop":
        print(" ".join(strings))
        break

    token = data.split()
    command = token[0]

    if command == "Delete":
        index = int(token[1])
        strings = delete(strings, index)

    elif command == "Swap":
        word_1, word_2 = token[1], token[2]
        strings = swap(strings, word_1, word_2)

    elif command == "Put":
        word = token[1]
        index = int(token[2])
        strings = put(strings, word, index)

    elif command == "Sort":
        strings = sorting(strings)

    elif command == "Replace":
        word_1, word_2 = token[1], token[2]
        strings = replace(strings, word_1, word_2)
