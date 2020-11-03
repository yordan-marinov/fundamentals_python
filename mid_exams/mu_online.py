rooms = input().split("|")

MAX_HEALTH = 100

current_health = 100
bitcoins = 0
is_dead = False
for index, room in enumerate(rooms, 1):
    token = room.split()
    name = token[0]
    value = int(token[1])

    if name == "potion":
        if current_health + value > MAX_HEALTH:
            value = MAX_HEALTH - current_health

        current_health += value
        print(f"You healed for {value} hp.")
        print(f"Current health: {current_health} hp.")

    elif name == "chest":
        print(f"You found {value} bitcoins.")
        bitcoins += value

    else:
        current_health -= value

        if current_health > 0:
            print(f"You slayed {name}.")
        else:
            print(f"You died! Killed by {name}.")
            print(f"Best room: {index}")
            is_dead = True
            break


if not is_dead:
    print(
        f"You've made it!\n"
        f"Bitcoins: {bitcoins}\n"
        f"Health: {current_health}"
    )
