numbers = map(str, input().split())

biggest_number = "".join(sorted(numbers, reverse=True))

print(biggest_number)
