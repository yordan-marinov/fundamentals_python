rooms = int(input())


free_chairs = 0
flag = True
for room in range(1, rooms + 1):

    data = input().split()
    representing_chairs = data[0]
    taken_chairs = int(data[1])

    if taken_chairs > len(representing_chairs):
        needed_chairs = taken_chairs - len(representing_chairs)
        print(f"{needed_chairs} more chairs needed in room {room}")
        flag = False

    free_chairs += len(representing_chairs) - taken_chairs


if flag:
    print(f"Game On, {free_chairs} free chairs left")
