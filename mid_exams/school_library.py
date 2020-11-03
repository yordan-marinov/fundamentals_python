def add_book(lst, name):
    if name not in lst:
        lst.insert(0, name)

    return lst


def take_book(lst, name):
    if name in lst:
        lst.remove(name)

    return lst


def swap_books(lst, name_1, name_2):
    if name_1 in lst and name_2 in lst:
        index_1, index_2 = lst.index(name_1), lst.index(name_2)

        lst[index_1], lst[index_2] = lst[index_2], lst[index_1]

    return lst


def insert_book(lst, name):
    lst.append(name)

    return lst


def check_book(lst, i):
    if i in range(len(lst)):
        print(lst[i])

    return lst


library = input().split("&")


while True:

    token = input()

    if token == "Done":
        print(", ".join(library))
        break

    command = token.split(" | ")

    if command[0] == "Add Book":
        book_name = command[1]
        library = add_book(library, book_name)

    elif command[0] == "Take Book":
        book_name = command[1]
        library = take_book(library, book_name)

    elif command[0] == "Swap Books":
        book_1, book_2 = command[1], command[2]
        library = swap_books(library, book_1, book_2)

    elif command[0] == "Insert Book":
        book_name = command[1]
        library = insert_book(library, book_name)

    elif command[0] == "Check Book":
        index = int(command[1])
        library = check_book(library, index)
