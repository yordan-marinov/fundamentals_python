def collect(lst, i):
    if i not in lst:
        lst.append(i)
    return lst


def drop(lst, i):
    if i in lst:
        lst.remove(i)
    return lst


def combine(lst, items):
    old_item, new_item = items.split(":")
    if old_item in lst:
        index = lst.index(old_item)
        lst.insert_number(index + 1, new_item)
    return lst


def renew(lst, i):
    if i in lst:
        given_item = lst.pop(lst.index(i))
        lst.append(given_item)
    return lst


collecting_items = input().split(", ")


while True:
    data = input()
    if data == "Craft!":
        break

    command, item = data.split(" - ")

    if command == "Collect":
        collecting_items = collect(collecting_items, item)

    elif command == "Drop":
        collecting_items = drop(collecting_items, item)

    elif command == "Combine Items":
        collecting_items = combine(collecting_items, item)

    elif command == "Renew":
        collecting_items = renew(collecting_items, item)


print(", ".join(collecting_items))
