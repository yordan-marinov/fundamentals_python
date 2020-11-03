events = input().split("|")

MAX_ENERGY = 100

energy = 100
coins = 100
day = True

for event in events:
    token = event.split("-")
    command_ingredient = token[0]
    number = int(token[1])

    if command_ingredient == "rest":
        if energy + number < MAX_ENERGY:
            current_energy = number
        else:
            current_energy = MAX_ENERGY - energy
        energy += current_energy
        print(f"You gained {current_energy} energy.")
        print(f"Current energy: {energy}.")

    elif command_ingredient == "order":

        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins > number:
            coins -= number
            print(f"You bought {command_ingredient}.")
        else:
            print(f"Closed! Cannot afford {command_ingredient}.")
            day = False
            break

if day:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
