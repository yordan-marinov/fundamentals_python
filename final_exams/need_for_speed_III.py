from collections import defaultdict


def get_data(count: int):
    result = defaultdict(lambda: defaultdict(int))

    for _ in range(count):
        data = input().split("|")
        car_name = data.pop(0)
        mileage = int(data[0])
        fuel = int(data[1])
        
        for info in CAR_INFO:
            if info == CAR_INFO[0]:
                result[car_name][info] = mileage
            else:
                result[car_name][info] = fuel

    return result


def drive(dd: dict, *args) -> dict:
    car = args[0]
    distance = int(args[1])
    current_fuel = int(args[2])
    mileage, fuel = CAR_INFO

    if dd[car][fuel] >= current_fuel:
        dd[car][mileage] += distance
        dd[car][fuel] -= current_fuel
        print(
            f"{car} driven for {distance} kilometers. "
            f"{current_fuel} liters of fuel consumed."
        )
        if dd[car][mileage] >= MAX_MILEAGE:
            print(
                f"Time to sell the {car}!"
            )
            del dd[car]
    else:
        print("Not enough fuel to make that ride")

    return dd


def refuel(dd: dict, *args) -> dict:
    car = args[0]
    current_fuel = int(args[1])
    fuel = CAR_INFO[1]

    if current_fuel + dd[car][fuel] > MAX_FUEL:
        current_fuel = MAX_FUEL - dd[car][fuel]

    dd[car][fuel] += current_fuel
    print(f"{car} refueled with {current_fuel} liters")

    return dd


def revert(dd: dict, *args) -> dict:
    car = args[0]
    kilometers = int(args[1])
    mileage = CAR_INFO[0]

    dd[car][mileage] -= kilometers

    if dd[car][mileage] > MIN_MILEAGE:
        print(
            f"{car} mileage decreased by {kilometers} kilometers"
        )
    else:
        dd[car][mileage] = MIN_MILEAGE

    return dd


def printing_statement(dd: dict):
    mileage, fuel = CAR_INFO

    for car, info in sorted(
            dd.items(),
            key=lambda x: (-x[1]["mileage"], x[0])
    ):
        print(
            f"{car} -> Mileage: {info[mileage]} kms, "
            f"Fuel in the tank: {info[fuel]} lt."
        )


cars_count = int(input())

MAX_MILEAGE = 100_000
MAX_FUEL = 75
MIN_MILEAGE = 10_000
CAR_INFO = ["mileage", "fuel"]

COMMANDS = {
    "Drive": drive,
    "Refuel": refuel,
    "Revert": revert,
}

cars = get_data(cars_count)

while True:

    token = input()
    if token == "Stop":
        printing_statement(cars)
        break

    token = token.split(" : ")
    command = token.pop(0)

    # if command == "Drive":
    #     cars = drive(cars, *token)
    #
    # elif command == "Refuel":
    #     cars = refuel(cars, *token)
    #
    # elif command == "Revert":
    #     cars = revert(cars, *token)

    cars = COMMANDS[command](cars, *token)
