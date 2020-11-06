def include(lst, shop):
    lst.append(shop)
    return lst

def visit(lst, direction, shops_count):
    shops_count = int(shops_count)

    if shops_count <= len(lst):
        if direction == "first":
            return lst[shops_count:]

        elif direction == "last":
            return lst[:- shops_count]

    return lst

def prefer(lst, i, ii):
    index_1 = int(i)
    index_2 = int(ii)
    if index_1 in range(len(lst)) and index_2 in range(len(lst)):
        lst[index_1], lst[index_2] = lst[index_2], lst[index_1]

    return lst


def place(lst, shop, index):
    index = int(index)
    if index in range(len(lst)):
        lst.insert(index + 1, shop)

    return lst


shops = input().split()
commands_count = int(input())

for _ in range(commands_count):

    command, *token = input().split()

    if command == "Include":
        shops = include(shops, *token)

    elif command == "Visit":
        shops = visit(shops, *token)

    elif command == "Prefer":
        shops = prefer(shops, *token)

    elif command == "Place":
        shops = place(shops, *token)

print("Shops left:")
print(*shops)
