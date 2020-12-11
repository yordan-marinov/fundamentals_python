def get_heroes_data() -> dict:
    number_heroes = int(input())

    heroes_data = {}
    for _ in range(number_heroes):
        data = input().split()
        hero_name = data[0]
        hit_points = int(data[1])
        mana_points = int(data[2])

        heroes_data[hero_name] = {
            "hp": hit_points,
            "mp": mana_points,
        }

    return heroes_data


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
            f"{hero_name} was hit for {damage} HP by {attacker} and "
            f"now has {dd[hero_name]['hp']} HP left!"
        )
    else:
        print(f"{hero_name} has been killed by {attacker}!")
        del dd[hero_name]

    return dd


def recharge(dd: dict, *args) -> dict:
    hero_name = args[0]
    amount = int(args[1])

    if dd[hero_name]["mp"] + amount > MAXIMUM_POINTS["mp"]:
        amount = MAXIMUM_POINTS["mp"] - dd[hero_name]["mp"]

    print(f"{hero_name} recharged for {amount} MP!")
    dd[hero_name]["mp"] += amount

    return dd


def heal(dd: dict, *args) -> dict:
    hero_name = args[0]
    amount = int(args[1])

    if dd[hero_name]["hp"] + amount > MAXIMUM_POINTS["hp"]:
        amount = MAXIMUM_POINTS["hp"] - dd[hero_name]["hp"]

    print(f"{hero_name} healed for {amount} HP!")
    dd[hero_name]["hp"] += amount

    return dd


def main_manipulation_print_func(dd: dict, commands) -> print:
    while True:

        data = input()
        if data == "End":
            sorting_printing_func(dd)
            break

        data = data.split(" - ")
        command = data.pop(0)

        commands[command](dd, *data)


def sorting_printing_func(dd: dict) -> print:
    for name, values in sorted(
            dd.items(),
            key=lambda pair: (-pair[1]["hp"], pair[0])
    ):
        print(f"{name}")
        print(f"  HP: {values['hp']}")
        print(f"  MP: {values['mp']}")


MAXIMUM_POINTS = {"hp": 100, "mp": 200}
COMMANDS = dict(
    CastSpell=cast_spell,
    TakeDamage=take_damage,
    Recharge=recharge,
    Heal=heal
)

heroes = get_heroes_data()
main_manipulation_print_func(heroes, COMMANDS)
