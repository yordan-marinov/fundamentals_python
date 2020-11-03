def read_data():
    numbers = [int(i) for i in input().split()]
    bomb_numbers = [int(j) for j in input().split()]
    return numbers, bomb_numbers


def detonation_bomb(data):
    lst = data[0]
    bomb = int(data[1][0])
    power = int(data[1][1])

    while bomb in lst:
        bomb_index = lst.index(int(data[1][0]))

        start = bomb_index - power
        if start < 0:
            start = 0

        end = bomb_index + power
        if end > len(lst):
            end = len(lst) - 1

        del lst[start:end + 1]

    return sum(lst)


print(detonation_bomb(read_data()))
