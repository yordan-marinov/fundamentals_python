def get_cars_info(cars_count: int) -> dict:
    cars_data = {}
    for _ in range(cars_count):
        data = input().split("|")
        car_name = data[0]
        mileage = int(data[1])
        fuel = int(data[2])

        cars_data[car_name] = {
            "mileage": mileage,
            "fuel": fuel
        }

    return cars_data


def print_statement(dd: dict) -> print:
    for name, values in sorted(
            dd.items(), key=lambda pair: (-pair[1]["mileage"], pair[0])
    ):
        print(
            f"{name} -> Mileage: {values['mileage']} kms, "
            f"Fuel in the tank: {values['fuel']} lt."
        )


def main_manipulation_printing_func(dd: dict):
    while True:

        data = input()
        if data == "Stop":
            print_statement(dd)
            break

        data = data.split(" : ")
        command = data.pop(0)

        COMMANDS[command](dd, *data)


def drive(dd: dict, *args) -> dict:
    current_car = args[0]
    distance = int(args[1])
    current_fuel = int(args[2])

    if dd[current_car]["fuel"] < current_fuel:
        print("Not enough fuel to make that ride")
    else:
        dd[current_car]["fuel"] -= current_fuel
        dd[current_car]["mileage"] += distance
        print(
            f"{current_car} driven for {distance} kilometers. "
            f"{current_fuel} liters of fuel consumed."
        )

    if dd[current_car]["mileage"] >= MAXIMUM_MILEAGE:
        print(f"Time to sell the {current_car}!")
        del dd[current_car]

    return dd


def refuel(dd: dict, *args) -> dict:
    current_car = args[0]
    current_fuel = int(args[1])

    if dd[current_car]["fuel"] + current_fuel > FUEL_TANK_CAPACITY:
        current_fuel = FUEL_TANK_CAPACITY - dd[current_car]["fuel"]

    print(f"{current_car} refueled with {current_fuel} liters")

    dd[current_car]["fuel"] += current_fuel

    return dd


def revert(dd: dict, *args) -> dict:
    current_car = args[0]
    current_kilometers = int(args[1])

    dd[current_car]["mileage"] -= current_kilometers

    if dd[current_car]["mileage"] < MINIMUM_MILEAGE:
        dd[current_car]["mileage"] = MINIMUM_MILEAGE
        return dd

    print(
        f"{current_car} mileage decreased by "
        f"{current_kilometers} kilometers"
    )

    return dd


COMMANDS = {
    "Drive": drive,
    "Refuel": refuel,
    "Revert": revert,
}
MAXIMUM_MILEAGE = 100_000
MINIMUM_MILEAGE = 10_000
FUEL_TANK_CAPACITY = 75

cars_number_count = int(input())
cars: dict = get_cars_info(cars_number_count)
main_manipulation_printing_func(cars)
