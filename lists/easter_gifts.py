gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break

    command = command.split()
    if (
            command[0] == "OutOfStock" and
            command[1] in gifts
    ):
        for index, gift in enumerate(gifts):
            if gift == command[1]:
                gifts[index] = "None"

    elif (
            command[0] == "Required" and
            int(command[2]) in range(len(gifts) + 1)
    ):
        gifts[int(command[2])] = command[1]

    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

print(" ".join([i for i in gifts if i != "None"]))
