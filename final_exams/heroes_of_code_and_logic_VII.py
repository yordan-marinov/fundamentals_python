def get_heroes_data() -> dict:
    heroes_data = {}
    for _ in range(number_of_heroes):
        data = input().split()
        name = data[0]
        hp = int(data[1])
        mp = int(data[2])

        heroes_data[name] = {"hp": hp, "mp": mp}

    return heroes_data


def main_manipulation_printing_func(dd: dict):
    while True:

        data = input()
        if data == "End":
            sorting_printing_statement(heroes)
            break

        data = data.split(" - ")
        command = data.pop(0)

        COMMANDS[command](dd, *data)


def cast_spell(dd: dict, *args) -> dict:
    hero_name = args[0]
    mp_needed = int(args[1])
    spell_name = args[2]

    if dd[hero_name]["mp"] >= mp_needed:
        dd[hero_name]["mp"] -= mp_needed
        print(
            f"{hero_name} has successfully cast {spell_name} "
            f"and now has {dd[hero_name]['mp']} MP!"
        )
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    return dd


def take_damage(dd: dict, *args) -> dict:
    hero_name = args[0]
    damage = int(args[1])
    attacker = args[2]

    dd[hero_name]["hp"] -= damage

    if dd[hero_name]["hp"] > 0:
        print(
            f"{hero_name} was hit for {damage} HP by {attacker} "
            f"and now has {dd[hero_name]['hp']} HP left!"
        )
    else:
        print(f"{hero_name} has been killed by {attacker}!")
        del dd[hero_name]

    return dd


def recharge(dd: dict, *args) -> dict:
    hero_name = args[0]
    amount = int(args[1])

    if dd[hero_name]["mp"] + amount > MAXIMUM_HP_MP_POINTS["mp"]:
        amount = MAXIMUM_HP_MP_POINTS["mp"] - dd[hero_name]["mp"]

    dd[hero_name]["mp"] += amount
    print(f"{hero_name} recharged for {amount} MP!")

    return dd


def heal(dd: dict, *args) -> dict:
    hero_name = args[0]
    amount = int(args[1])

    if dd[hero_name]["hp"] + amount > MAXIMUM_HP_MP_POINTS["hp"]:
        amount = MAXIMUM_HP_MP_POINTS["hp"] - dd[hero_name]["hp"]

    dd[hero_name]["hp"] += amount
    print(f"{hero_name} healed for {amount} HP!")

    return dd


def sorting_printing_statement(dd: dict) -> print:
    for name, values in sorted(
            dd.items(),
            key=lambda pair: (-pair[1]["hp"], pair[0])
    ):
        print(f"{name}")
        print(f"  HP: {values['hp']}")
        print(f"  MP: {values['mp']}")


MAXIMUM_HP_MP_POINTS = {
    "hp": 100,
    "mp": 200,
}

COMMANDS = {
    "CastSpell": cast_spell,
    "TakeDamage": take_damage,
    "Recharge": recharge,
    "Heal": heal,
}

number_of_heroes = int(input())

heroes: dict = get_heroes_data()
main_manipulation_printing_func(heroes)
