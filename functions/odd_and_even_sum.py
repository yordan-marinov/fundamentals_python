def odd_sum(numbers: str):
    return sum([int(n) for n in numbers if int(n) % 2 != 0])


def even_sum(numbers: str):
    return sum([int(n) for n in numbers if int(n) % 2 == 0])


num = input()

print(f"Odd sum = {odd_sum(num)}, Even sum = {even_sum(num)}")
