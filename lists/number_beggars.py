numbers = list(map(int, input().split(", ")))
beggars = [0] * int(input())


index = 0
for number in numbers:
    beggars[index] += number
    index += 1
    if index == len(beggars):
        index = 0

print(beggars)
