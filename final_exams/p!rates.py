def increase_values(lst_1, lst_2) -> list:
    return [
        sum(pairs)
        for pairs in zip(lst_1, lst_2)
    ]


def cities_map() -> dict:
    result = {}
    while True:

        data = input()
        if data == "Sail":
            break

        data = data.split("||")
        name = data.pop(0)
        population_gold = [int(i) for i in data]

        if name not in result:
            result[name] = population_gold
        else:
            result[name] = increase_values(result[name], population_gold)

    return result


def plunder(cities_dict: dict, city: str, *args) -> dict:
    population_gold = [int(e) for e in args]

    if city in cities_dict:
        print(
            f"{city} plundered! "
            f"{population_gold[1]} gold stolen, "
            f"{population_gold[0]} citizens killed."
        )

        cities_dict[city] = [
            p - g
            for p, g in zip(cities_dict[city], population_gold)
        ]

        for v in cities_dict[city]:
            if v <= 0:
                print(f"{city} has been wiped off the map!")
                del cities_dict[city]
                continue

    return cities_dict


def prosper(cities_dict: dict, city: str, gold: int) -> dict:
    if gold > 0:
        population_gold = [0, gold]
        cities_dict[city] = increase_values(cities_dict[city], population_gold)
        print(
            f"{gold} gold added to the city treasury. "
            f"{city} now has {cities_dict[city][1]} gold."
        )

    else:
        print("Gold added cannot be a negative number!")

    return cities_dict


cities: dict = cities_map()

while True:

    token = input()
    if token == "End":
        break

    token = token.split("=>")
    command = token.pop(0)
    town = token.pop(0)
    data = [int(i) for i in token]

    if command == "Plunder":
        cities = plunder(cities, town, *data)

    elif command == "Prosper":
        gold = int(*data)
        cities = prosper(cities, town, gold)

if cities:
    print(
        f"Ahoy, Captain! "
        f"There are {len(cities)} wealthy settlements to go to:"
    )

    for town, value in sorted(cities.items(), key=lambda x: (-x[1][1], x[0])):
        print(
            f"{town} -> Population: {value[0]} citizens, Gold: {value[1]} kg"
        )
else:
    print(
        "Ahoy, Captain! "
        "All targets have been plundered and destroyed!"
    )
