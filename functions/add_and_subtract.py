def add_number(*args):
    return sum(args)


def subtract(num_1, num_2):
    return num_1 - num_2


def add_and_subtract(func):
    return func


n_1 = int(input())
n_2 = int(input())
n_3 = int(input())

print(
    add_and_subtract(
        subtract(
            add_number(n_1, n_2), n_3)
    )
)
