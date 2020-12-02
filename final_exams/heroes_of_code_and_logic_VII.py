def get_data() -> dict:
    heroes_count = int(input())

    heroes = {}
    for _ in range(heroes_count):
        hero_data = input().split()

        name = hero_data[0]
        hit_points = int(hero_data[1])
        mana_points = int(hero_data[2])

        hero = {}
        for key in MAXIMUM_POINTS.keys():
            if key == "hp":
                hero[key] = hit_points
            else:
                hero[key] = mana_points

        heroes[name] = hero

    return heroes


def cast_spell(dd: dict, *args) -> dict:
    hero_name = args[0]
    mp_needed = int(args[1])
    spell_name = args[2]
    mana_points = "mp"

    if dd[hero_name][mana_points] >= mp_needed:
        dd[hero_name][mana_points] -= mp_needed
        print(
            f"{hero_name} has successfully cast {spell_name} and "
            f"now has {dd[hero_name][mana_points]} MP!"
        )

    else:
        print(
            f"{hero_name} does not have enough MP to cast {spell_name}!"
        )

    return dd


def take_damage(dd: dict, *args) -> dict:
    hero_name = args[0]
    damage = int(args[1])
    attacker = args[2]
    hit_points = "hp"

    dd[hero_name][hit_points] -= damage

    if dd[hero_name][hit_points] > 0:
        print(
            f"{hero_name} was hit for {damage} HP by {attacker} and "
            f"now has {dd[hero_name][hit_points]} HP left!"
        )
    else:
        del dd[hero_name]
        print(f"{hero_name} has been killed by {attacker}!")

    return dd


def recharge(dd: dict, *args) -> dict:
    hero_name = args[0]
    amount = int(args[1])
    mana_points = "mp"
    recharged_amount = 0

    if dd[hero_name][mana_points] + amount > MAXIMUM_POINTS[mana_points]:
        recharged_amount += MAXIMUM_POINTS[mana_points] - dd[hero_name][mana_points]
    else:
        recharged_amount += amount

    dd[hero_name][mana_points] += recharged_amount
    print(f"{hero_name} recharged for {recharged_amount} MP!")

    return dd


def heal(dd: dict, *args) -> dict:
    hero_name = args[0]
    amount = int(args[1])
    hit_points = "hp"
    healed_amount = 0

    if dd[hero_name][hit_points] + amount > MAXIMUM_POINTS[hit_points]:
        healed_amount += MAXIMUM_POINTS[hit_points] - dd[hero_name][hit_points]
    else:
        healed_amount += amount

    dd[hero_name][hit_points] += healed_amount
    print(f"{hero_name} healed for {healed_amount} HP!")

    return dd


def print_statement(dd: dict) -> print:
    for name, key_value in sorted(dd.items(), key=lambda c: (-c[1]["hp"], c[0])):
        print(f"{name}")

        for key, value in key_value.items():
            print(f"  {key.upper()}: {value}")


def final_result(dd: dict):
    while True:

        data = input()
        if data == "End":
            print_statement(dd)
            break

        data = data.split(" - ")
        command = data.pop(0)

        COMMANDS[command](dd, *data)


MAXIMUM_POINTS = {
    "hp": 100,
    "mp": 200,
}

COMMANDS = {
    "CastSpell": cast_spell,
    "TakeDamage": take_damage,
    "Recharge": recharge,
    "Heal": heal,
}

party: dict = get_data()
final_result(party)
