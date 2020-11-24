from functools import reduce
strings = input()

# cool_threshold = sum([int(n) for n in strings if n.isdigit()])
cool_threshold = reduce(lambda x, y: x * y, [int(n) for n in strings if n.isdigit()])

print(cool_threshold)