def include(lst, item):
    return lst + item


def visit(lst, items):
    data = items
    shop = data[0]
    number_of_shops = int(data[1])

    if len(lst) >= number_of_shops:
        if shop == "first":
            lst = [i for i in lst[number_of_shops:]]
        else:
            lst = [i for i in lst[:-number_of_shops]]

    return lst


def prefer(lst, items):
    index_1, index_2 = [int(i) for i in items]
    if index_1 in range(len(lst)) and index_2 in range(len(lst)):
        lst[index_1], lst[index_2] = lst[index_2], lst[index_1]

    return lst


def place(lst, items):
    data = items
    shop = data[0]
    index = int(data[1]) + 1

    if index in range(len(lst)):
        lst.insert(index, shop)

    return lst



shops = input().split()
commands_count = int(input())

for _ in range(commands_count):
    data = input().split()
    command = data.pop(0)

    if command == "Include":
        shops = include(shops, data)

    elif command == "Visit":
        shops = visit(shops, data)

    elif command == "Prefer":
        shops = prefer(shops, data)

    elif command == "Place":
        shops = place(shops, data)



print(
    f"Shops left:\n"
    f"{' '.join(shops)}"
)
