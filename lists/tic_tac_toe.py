def read_list_integers(separate=" "):
    return [int(n) for n in input().split(separate)]


def primary_diagonal_sum(size_n: int, mat_rix):
    result = 0
    for i in range(size):
        result += mat_rix[i][i]
    return result


size = int(input())

matrix = [
    read_list_integers()
    for _ in range(size)
]

print(primary_diagonal_sum(size, matrix))
