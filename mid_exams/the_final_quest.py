def delete_word(lst, index):
    index = int(index)
    if index + 1 in range(len(lst)):
        del lst[index + 1]

    return lst


def swap(lst, word_1, word_2):
    if word_1 in lst and word_2 in lst:
        i_1, i_2 = lst.index(word_1), lst.index(word_2)
        lst[i_1], lst[i_2] = lst[i_2], lst[i_1]

    return lst


def put(lst, word, index):
    index = int(index)
    if index - 1 in range(1, len(lst) + 1):
        if index == len(lst) - 1:
            lst.append(word)
        else:
            lst.insert(index - 1, word)

    return lst


def sort_words(lst):
    return sorted(lst, reverse=True)


def replace(lst, word_1, word_2):
    if word_2 in lst:
        lst[lst.index(word_2)] = word_1

    return lst


words = input().split()

while True:

    data = input()
    if data == "Stop":
        print(*words)
        break

    command, *items = data.split()

    if command == "Delete":
        words = delete_word(words, *items)

    elif command == "Swap":
        words = swap(words, *items)

    elif command == "Put":
        words = put(words, *items)

    elif command == "Sort":
        words = sort_words(words)

    elif command == "Replace":
        words = replace(words, *items)
