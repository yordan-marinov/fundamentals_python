def add(dd: dict, *args) -> dict:
    name = args[0]
    current_health = int(args[1])
    current_energy = int(args[2])

    if name not in dd:
        dd[name] = {"health": current_health, "energy": current_energy}
    else:
        dd[name]["health"] += current_health

    return dd


def attacker(dd: dict, *args) -> dict:
    attacker_name = args[0]
    defender_name = args[1]
    damage = int(args[2])

    if attacker_name in dd and defender_name in dd:
        dd[defender_name]["health"] -= damage
        if dd[defender_name]["health"] <= 0:
            print(f"{defender_name} was disqualified!")
            del dd[defender_name]

        dd[attacker_name]["energy"] -= 1
        if dd[attacker_name]['energy'] <= 0:
            print(f"{attacker_name} was disqualified!")
            del dd[attacker_name]

    return dd


def delete_name(dd: dict, *args) -> dict:
    current_name = args[0]

    if current_name in dd:
        del dd[current_name]
    elif current_name == "All":
        dd.clear()

    return dd


def sorting_printing_func(dd: dict) -> print:
    print(f"People count: {len(dd)}")

    for name, values in sorted(
            dd.items(),
            key=lambda pair: (-pair[1]["health"], pair[0])
    ):
        print(f"{name} - {values['health']} - {values['energy']}")


COMMANDS = {
    "Add": add,
    "Attack": attacker,
    "Delete": delete_name,
}

people = {}

while True:
    data = input()
    if data == "Results":
        sorting_printing_func(people)
        break

    data = data.split(":")
    command = data.pop(0)

    COMMANDS[command](people, *data)
