numbers = list(map(int, input().split()))
smallest_count = int(input())


for _ in range(smallest_count):
    numbers.remove(min(numbers))

print(numbers)
