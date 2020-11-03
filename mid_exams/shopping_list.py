def urgent(lst, item):
    if item not in lst:
        lst.insert_number(0, item)
    return lst


def unnecessary(lst, element):
    if element in lst:
        lst.remove(element)
    return lst


def correct(lst, old_item, new_item):
    if old_item in lst:
        i = lst.index(old_item)
        lst[i] = new_item
    return lst


def rear_range(lst, element):
    if element in lst:
        index = lst.index(element)
        e = lst.pop(index)
        lst.append(e)
    return lst


shopping_list = input().split("!")


while True:
    command = input()
    if command == "Go Shopping!":
        break

    token = command.split()
    cmd = token[0]
    item = token[1]

    if cmd == "Urgent":
        shopping_list = urgent(shopping_list, item)

    elif cmd == "Unnecessary":
        shopping_list = unnecessary(shopping_list, item)

    elif cmd == "Correct":
        item_new = token[2]
        shopping_list = correct(shopping_list, item, item_new)

    else:
        shopping_list = rear_range(shopping_list, item)


print(", ".join(shopping_list))
