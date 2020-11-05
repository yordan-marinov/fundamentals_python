def add_book(lst, item):
    if item not in lst:
        lst.insert(0, item)

    return lst


def take_book(lst, item):
    while item in lst:
        lst.remove(item)

    return lst


def swap_books(lst, book_1, book_2):
    if book_1 in lst and book_2 in lst:
        index_1, index_2 = lst.index(book_1), lst.index(book_2)
        lst[index_1], lst[index_2] = lst[index_2], lst[index_1]

    return lst


def insert_book(lst, item):
    lst.append(str(item))
    return lst


def check_book(lst, item):
    index = int(item)
    if index in range(len(lst)):
        print(lst[index])

    return lst


book_shelf = input().split("&")

while True:

    data = input()
    if data == "Done":
        print(", ".join(book_shelf))
        break

    command, *books = data.split(" | ")

    commands = {
        "Add Book": add_book,
        "Take Book": take_book,
        "Swap Books": swap_books,
        "Insert Book": insert_book,
        "Check Book": check_book,
    }

    book_shelf = commands[command](book_shelf, *books)
