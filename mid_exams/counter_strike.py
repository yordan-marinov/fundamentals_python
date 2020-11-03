initial_energy = int(input())

wins_counter = 0
flag = False
while True:
    command = input()
    if command == "End of battle":
        break

    distance = int(command)
    if initial_energy < distance:
        print(f"Not enough energy! Game ends with {wins_counter} won battles and {initial_energy} energy")
        flag = True
        break

    wins_counter += 1
    initial_energy -= distance

    if wins_counter % 3 == 0:
        initial_energy += wins_counter

if not flag:
    print(f"Won battles: {wins_counter}. Energy left: {initial_energy}")
