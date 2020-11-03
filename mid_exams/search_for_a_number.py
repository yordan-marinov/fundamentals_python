numbers = [int(n) for n in input().split()]

data = [int(n) for n in input().split()]

numbers = numbers[:data[0]]
numbers = numbers[data[1]:]

if data[2] in numbers:
    print("YES!")
else:
    print("NO!")
