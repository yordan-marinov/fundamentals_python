def out_of_stock(lst, gift):
    while gift in lst:
        lst[lst.index(gift)] = "None"

    return lst


def required(lst, gift, index):
    index = int(index)
    if index in range(len(lst)):
        lst[index] = gift

    return lst


def just_in_case(lst, gift):
    lst[-1] = gift
    return lst


gifts = input().split()

while True:

    data = input()
    if data == "No Money":
        print(*[g for g in gifts if g != "None"])
        break

    command, *items = data.split()

    commands = {
        "OutOfStock": out_of_stock,
        "Required": required,
        "JustInCase": just_in_case,
    }

    gifts = commands[command](gifts, *items)
