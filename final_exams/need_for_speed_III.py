def cars(n: int) -> dict:
    result = {}

    for _ in range(n):
        data = input().split("|")
        car = data[0]
        mileage = int(data[1])
        fuel = int(data[2])

        result[car] = {"mileage": mileage, "fuel": fuel}

    return result


def print_statement(dd: dict) -> print:
    for car, values in sorted(
            dd.items(),
            key=lambda pair: (-pair[1]["mileage"], pair[0])
    ):
        print(
            f"{car} -> Mileage: {values['mileage']} kms, "
            f"Fuel in the tank: {values['fuel']} lt."
        )


def main(dd: dict):
    while True:

        data = input()
        if data == "Stop":
            print_statement(dd)
            break

        data = data.split(" : ")
        command = data.pop(0)

        COMMANDS[command](dd, *data)


def drive(dd: dict, *args) -> dict:
    car = args[0]
    distance = int(args[1])
    fuel = int(args[2])

    if dd[car]["fuel"] < fuel:
        print("Not enough fuel to make that ride")
    else:
        dd[car]["mileage"] += distance
        dd[car]["fuel"] -= fuel
        print(
            f"{car} driven for {distance} kilometers. "
            f"{fuel} liters of fuel consumed."
        )

    if dd[car]["mileage"] >= MAXIMUM_MILEAGE:
        print(f"Time to sell the {car}!")
        del dd[car]

    return dd


def refuel(dd: dict, *args) -> dict:
    car = args[0]
    fuel = int(args[1])

    if dd[car]["fuel"] + fuel > FUEL_TANK_CAPACITY:
        fuel = FUEL_TANK_CAPACITY - dd[car]["fuel"]

    dd[car]["fuel"] += fuel
    print(f"{car} refueled with {fuel} liters")

    return dd


def revert(dd: dict, *args) -> dict:
    car = args[0]
    kilometers = int(args[1])

    dd[car]["mileage"] -= kilometers
    print(
        f"{car} mileage decreased by {kilometers} kilometers"
    )

    if dd[car]["mileage"] < MINIMUM_MILEAGE:
        dd[car]["mileage"] = MINIMUM_MILEAGE

    return dd


COMMANDS = {
    "Drive": drive,
    "Refuel": refuel,
    "Revert": revert,
}

MAXIMUM_MILEAGE = 100_000
MINIMUM_MILEAGE = 10_000
FUEL_TANK_CAPACITY = 75

cars_count = int(input())
main(cars(cars_count))