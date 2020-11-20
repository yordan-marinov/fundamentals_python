start = ord(input())
end = ord(input())

random_string = [ord(s) for s in input()]
in_between_sum = sum([
    c
    for c in random_string
    if c in range(start + 1, end)
])

print(in_between_sum)
