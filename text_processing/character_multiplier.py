from itertools import zip_longest


def multiply_elements(*args: str) -> int:
    result = 1
    for number in args:
        result *= number
    return result


data = input().split()
#
# total = 0
# for pair in zip_longest(data[0], data[1]):
#     total += multiply_elements(*[ord(e) for e in pair if e != None])
#
# print(total)
print(
    sum(
        [
            multiply_elements(*[ord(e) for e in pair if e is not None])
            for pair in zip_longest(data[0], data[1])
        ]
    )
)
