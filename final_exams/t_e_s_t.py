from collections import defaultdict

cars = defaultdict(lambda : defaultdict(int))
info = ["mileage", "petrol"]
n = int(input())

for _ in range(n):
    data = input().split("|")
    car_name = data.pop(0)
    mileage = int(data[0])
    petrol = int(data[1])

    for i in info:
        if i == info[0]:
            cars[car_name][i] = mileage
        else:
            cars[car_name][i] = petrol

print(cars)