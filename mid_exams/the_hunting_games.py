days = int(input())
players = int(input())
energy_group = float(input())
water_person = float(input())
food_person = float(input())

water_group = water_person * players * days
food_group = food_person * players * days

flag = True
for day in range(1, days + 1):
    energy_loss = float(input())
    energy_group -= energy_loss

    if energy_group <= 0:
        flag = False
        break

    if day % 2 == 0:
        energy_group *= 1.05
        water_group *= 0.7

    if day % 3 == 0:
        energy_group *= 1.10
        food_group -= (food_group / players)

if flag:
    print(
        f"You are ready for the quest. "
        f"You will be left with - {energy_group:.2f} energy!"
    )
else:
    print(
        f"You will run out of energy. "
        f"You will be left with {food_group:.2f} food "
        f"and {water_group:.2f} water."
    )