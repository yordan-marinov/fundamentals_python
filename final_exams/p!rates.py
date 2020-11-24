from collections import defaultdict


def towns_data() -> dict:
    result = defaultdict(lambda: defaultdict(int))

    while True:

        data = input()
        if data == "Sail":
            break

        data = data.split("||")
        town = data[0]
        data_population = int(data[1])
        data_gold = int(data[2])

        for name in POPULATION_GOLD:
            if name == "population":
                result[town][name] += data_population
            else:
                result[town][name] += data_gold

    return result


def plunder(dd, *args) -> dict:
    town = args[0]
    people = int(args[1])
    gold = int(args[2])
    current_population = "population"
    current_gold = "gold"

    dd[town][current_population] -= people
    dd[town][current_gold] -= gold

    print(
        f"{town} plundered! "
        f"{gold} gold stolen, "
        f"{people} citizens killed."
    )
    if (
            (dd[town][current_population] <= POPULATION_GOLD[current_population]) or
            (dd[town][current_gold] <= POPULATION_GOLD[current_gold])
    ):
        print(f"{town} has been wiped off the map!")
        del dd[town]

    return dd


def prosper(dd, *args):
    town = args[0]
    gold = int(args[1])
    current_gold = "gold"

    if gold > 0:
        dd[town][current_gold] += gold

        print(
            f"{gold} gold added to the city treasury. "
            f"{town} now has {dd[town][current_gold]} gold."
        )
    else:
        print("Gold added cannot be a negative number!")

    return dd


def print_statement(dd: dict):
    if dd:
        remain_population = "population"
        remain_gold = "gold"

        print(
            f"Ahoy, Captain! There are {len(dd)} "
            f"wealthy settlements to go to:"
        )

        for key, value in sorted(
                dd.items(), key=lambda x: (-x[1]["gold"], x[0])
        ):
            print(
                f"{key} -> Population: {dd[key][remain_population]} citizens, "
                f"Gold: {dd[key][remain_gold]} kg"
            )
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


POPULATION_GOLD = {
    "population": 0,
    "gold": 0,
}

towns = towns_data()

while True:

    token = input()
    if token == "End":
        print_statement(towns)
        break

    token = token.split("=>")
    command = token.pop(0)

    if command == "Plunder":
        plunder(towns, *token)

    elif command == "Prosper":
        prosper(towns, *token)
