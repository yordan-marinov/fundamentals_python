def perfect_number(number: int):
    if number == sum(
            [divisor for divisor in range(1, number // 2 + 1) if number % divisor == 0]
    ):
        return "We have a perfect number!"
    return "It's not so perfect."


num = int(input())

print(perfect_number(num))
