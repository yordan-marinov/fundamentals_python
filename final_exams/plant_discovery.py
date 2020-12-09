import re


def rate(dd: dict, *args) -> dict:
    current_plant_name = args[0]
    current_plant_rating = int(args[1])

    dd[current_plant_name]["rating"].append(current_plant_rating)

    return dd


def update(dd: dict, *args) -> dict:
    current_plant_name = args[0]
    plant_new_rarity = int(args[1])

    dd[current_plant_name]["rarity"] = plant_new_rarity

    return dd


def reset(dd: dict, *args) -> dict:
    current_plant_name = args[0]

    dd[current_plant_name]["rating"].clear()

    return dd


def get_plants_data() -> dict:
    n = int(input())

    plants_data = {}
    for _ in range(n):
        data = input().split("<->")
        plant_name = data[0]
        plant_rarity = int(data[1])
        plant_ratings = []

        plants_data[plant_name] = {
            "rarity": plant_rarity,
            "rating": plant_ratings
        }

    return plants_data


def average_ratings(lst: list) -> int:
    try:
        return sum(lst) / len(lst)
    except:
        return 0


def sorting_printing_statement(dd: dict) -> print:
    print("Plants for the exhibition:")

    for plant, values in sorted(
            dd.items(), key=lambda pair: (
                    pair[1]["rarity"],
                    average_ratings(pair[1]["rating"])
            ), reverse=True
    ):
        print(
            f"- {plant}; "
            f"Rarity: {values['rarity']}; "
            f"Rating: {average_ratings(values['rating']):.2f}"
        )


def main_manipulation_print_func(dd: dict, commands) -> print:
    while True:

        data = input()
        if data == "Exhibition":
            sorting_printing_statement(dd)
            break

        data = re.split(r":\s|\s-\s", data)
        command = data.pop(0)

        try:
            commands[command](dd, *data)
        except:
            print("error")


COMMANDS = dict(Rate=rate, Update=update, Reset=reset)

plants = get_plants_data()
main_manipulation_print_func(plants, COMMANDS)
