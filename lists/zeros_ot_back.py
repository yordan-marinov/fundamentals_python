string = list(map(int, input().split(", ")))

print([n for n in string if n != 0] + [z for z in string if z == 0])
