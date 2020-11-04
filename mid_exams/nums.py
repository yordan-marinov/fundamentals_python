numbers = [int(n) for n in input().split()]

numbers = sorted(
    [
        num for num in numbers if
        num > sum(numbers) / len(numbers)
    ],
    reverse=True
)

if not numbers:
    print("No")
else:
    print(*numbers[:5])
