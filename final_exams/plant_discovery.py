from collections import defaultdict
import re


def get_data(n: int) -> dict:
    result = defaultdict(dict)

    for _ in range(n):
        data = input().split("<->")
        plant = data[0]
        rarity = int(data[1])

        result[plant]["rarity"] = rarity
        result[plant]["rating"] = []

    return result


def rate_rating(dd: dict, *args) -> dict:
    plant = args[0]
    rating = int(args[1])

    dd[plant]["rating"].append(rating)

    return dd


def update_rarity(dd: dict, *args) -> dict:
    plant = args[0]
    new_rarity = int(args[1])

    dd[plant]["rarity"] = new_rarity

    return dd


def reset_plant(dd: dict, *args) -> dict:
    plant = args[0]

    dd[plant]["rating"].clear()

    return dd


def average_ratings(lst: list) -> int:
    if len(lst) == 0:
        return 0

    return sum(lst) / len(lst)


def print_statement(dd: dict) -> print:
    print("Plants for the exhibition:")

    for plant, values in sorted(
            dd.items(),
            key=lambda pair_values: (
                    pair_values[1]["rarity"],
                    average_ratings(pair_values[1]["rating"]),
            ),
            reverse=True
    ):

        print(
            f"- {plant}; Rarity: "
            f"{values['rarity']}; "
            f"Rating: {average_ratings(values['rating']):.2f}"
        )


def main(dd: dict):
    while True:

        data = input()
        if data == "Exhibition":
            print_statement(dd)
            break

        data = re.split(r":\s+|\s-\s", data)
        command = data.pop(0)
        plant = data[0]

        if (
                plant not in dd or
                command not in COMMANDS
        ):
            print("error")
            continue

        COMMANDS[command](dd, *data)


COMMANDS = {
    "Rate": rate_rating,
    "Update": update_rarity,
    "Reset": reset_plant,
}

main(get_data(int(input())))
