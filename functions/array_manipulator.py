def min_even(lst):
    min_num = None
    min_index = None
    for i, n in enumerate(numbers):

        if (
                (n % 2 == 0) and
                (min_num is None or n <= min_num)
        ):
            min_num = n
            min_index = i
    return min_index


def min_odd(lst):
    min_num = None
    min_index = None
    for i, n in enumerate(lst):

        if (
                (n % 2 != 0) and
                (min_num is None or n <= min_num)
        ):
            min_num = n
            min_index = i

    return min_index


def max_even(lat):
    max_num = None
    max_index = None
    for i, n in enumerate(numbers):

        if (
                (n % 2 == 0) and
                (max_num is None or n >= max_num)
        ):
            max_num = n
            max_index = i
    return max_index


def max_odd(lst):
    max_num = None
    max_index = None
    for i, n in enumerate(lst):

        if (
                (n % 2 != 0) and
                (max_num is None or n >= max_num)
        ):
            max_num = n
            max_index = i

    return max_index


def odd_numbers(lst):
    return [n for n in lst if n % 2 != 0]


def even_numbers(lst):
    return [n for n in lst if n % 2 == 0]


numbers = [int(n) for n in input().split()]

while True:
    data = input()
    if data == "end":
        break

    token = data.split()
    command = token[0]

    if command == "exchange":
        index = int(token[1])
        if index in range(len(numbers)):
            numbers = numbers[index + 1:] + numbers[:index + 1]
        else:
            print("Invalid index")

    elif command == "max":
        element = token[1]

        odds_evens = {
            "odd": max_odd,
            "even": max_even,
        }

        max_even_odd_index = odds_evens[element](numbers)

        if max_even_odd_index is not None:
            print(max_even_odd_index)
        else:
            print("No matches")

    elif command == "min":
        element = token[1]

        odds_evens = {
            "odd": min_odd,
            "even": min_even
        }

        min_even_odd_index = odds_evens[element](numbers)

        if min_even_odd_index is not None:
            print(min_even_odd_index)
        else:
            print("No matches")

    elif command == "first":
        count = int(token[1])
        element = token[2]
        if count <= len(numbers):
            elements = {
                "odd": odd_numbers,
                "even": even_numbers,
            }
            print(elements[element](numbers)[:count])
        else:
            print("Invalid count")

    elif command == "last":
        count = int(token[1])
        element = token[2]
        if count <= len(numbers):
            elements = {
                "odd": odd_numbers,
                "even": even_numbers,
            }
            print(elements[element](numbers)[-count:])
        else:
            print("Invalid count")

print(numbers)
