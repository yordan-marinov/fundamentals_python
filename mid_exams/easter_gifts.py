def out_of_stock(lst, present):
    while present in lst:
        lst[lst.index(present)] = "None"

    return lst


def required(lst, present, i):
    if i in range(len(lst)):
        lst[i] = present

    return lst


def just_in_case(lst, present):
    lst[-1] = present

    return lst


gifts = input().split()

while True:

    data = input()
    if data == "No Money":
        print(" ".join(g for g in gifts if g != "None"))
        break

    token = data.split()
    command = token[0]
    gift = token[1]

    if command == "OutOfStock":
        gifts = out_of_stock(gifts, gift)

    elif command == "Required":
        index = int(token[2])
        gifts = required(gifts, gift, index)

    elif command == "JustInCase":
        gifts = just_in_case(gifts, gift)
