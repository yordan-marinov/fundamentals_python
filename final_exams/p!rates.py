def get_cities_data() -> dict:
    cities_data = {}

    while True:

        data = input()
        if data == "Sail":
            break

        data = data.split("||")
        city_name = data[0]
        population = int(data[1])
        gold = int(data[2])

        if city_name not in cities_data:
            cities_data[city_name] = {
                "population": population,
                "gold": gold
            }
        else:
            cities_data[city_name]["population"] += population
            cities_data[city_name]["gold"] += gold

    return cities_data


def main(dd: dict, commands: dict):
    while True:

        data = input()
        if data == "End":
            print_statement(dd)
            break

        data = data.split("=>")
        command = data.pop(0)

        commands[command](dd, *data)


def plunder(dd: dict, *args) -> dict:
    current_city_name = args[0]
    current_people = int(args[1])
    current_gold = int(args[2])

    dd[current_city_name]["population"] -= current_people
    dd[current_city_name]["gold"] -= current_gold

    print(
        f"{current_city_name} plundered! "
        f"{current_gold} gold stolen, "
        f"{current_people} citizens killed."
    )
    if (
            dd[current_city_name]["population"] <= 0 or
            dd[current_city_name]["gold"] <= 0
    ):
        print(f"{current_city_name} has been wiped off the map!")
        del dd[current_city_name]

    return dd


def prosper(dd: dict, *args) -> dict:
    current_city_name = args[0]
    current_gold = int(args[1])

    if current_gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        dd[current_city_name]["gold"] += current_gold
        print(
            f"{current_gold} gold added to the city treasury. "
            f"{current_city_name} now has "
            f"{dd[current_city_name]['gold']} gold."
        )
    return dd


def print_statement(dd: dict) -> print:
    print(
        f"Ahoy, Captain! "
        f"There are {len(dd)} wealthy settlements to go to:"
    )
    for city, values in sorted(
            dd.items(),
            key=lambda pair: (-pair[1]['gold'], pair[0])
    ):
        print(
            f"{city} -> Population: "
            f"{values['population']} citizens, "
            f"Gold: {values['gold']} kg"
        )


COMMANDS = {
    "Plunder": plunder,
    "Prosper": prosper,
}

cities = get_cities_data()
main(cities, COMMANDS)
