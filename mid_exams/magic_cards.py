def add_card(lst, new_lst, name):
    if name in lst:
        new_lst.append(name)
    else:
        print("Card not found.")

    return new_lst


def insert_card(lst, new_lst, name, index):
    index = int(index)
    if name in lst and index in range(len(new_lst)):
        new_lst.insert(index, name)
    else:
        print("Error!")

    return new_lst


def remove_card(new_lst, name):
    if name in new_lst:
        new_lst.remove(name)
    else:
        print("Card not found.")

    return new_lst


def swap_card(new_lst, name_1, name_2):
    i_1, i_2 = new_lst.index(name_1), new_lst.index(name_2)
    new_lst[i_1], new_lst[i_2] = new_lst[i_2], new_lst[i_1]

    return new_lst


cards = input().split(":")
new_cards = []
while True:

    data = input()
    if data == "Ready":
        print(*new_cards)
        break

    command, *token = data.split()

    if command == "Add":
        new_cards = add_card(cards, new_cards, *token)

    elif command == "Insert":
        new_cards = insert_card(cards, new_cards, *token)

    elif command == "Remove":
        new_cards = remove_card(new_cards, *token)

    elif command == "Swap":
        new_cards = swap_card(new_cards, *token)

    elif command == "Shuffle":
        new_cards = new_cards[::-1]
