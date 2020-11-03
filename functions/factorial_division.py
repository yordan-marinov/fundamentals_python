from functools import reduce


def factorial(number):
    return reduce(lambda a, b: a * b, range(1, number + 1))


def factorial_division(num_1, num_2):
    return f"{(factorial(num_1) / factorial(num_2)):.2f}"


n = int(input())
m = int(input())

print(factorial_division(n, m))
