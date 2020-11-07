needed_experience = float(input())
count_battles = int(input())

experience = 0
flag = False
for battle_number in range(1, count_battles + 1):

    current_experience = float(input())

    if battle_number % 3 == 0:
        current_experience *= 1.15

    if battle_number % 5 == 0:
        current_experience *= 0.9

    if battle_number % 15 == 0:
        current_experience *= 1.05

    experience += current_experience
    if experience >= needed_experience:
        flag = True
        print(
            f"Player successfully collected his needed experience "
            f"for {battle_number} battles."
        )
        break

if not flag:
   print(
       f"Player was not able to collect the needed experience, "
       f"{needed_experience - experience:.2f} more needed."
   )