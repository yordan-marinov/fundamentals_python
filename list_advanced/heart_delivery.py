neighborhood = [int(i) for i in input().split("@")]


current_index = 0
while True:
    command = input()
    if command == "Love!":
        break

    token = command.split()
    index = int(token[1])
    current_index += index

    if current_index > len(neighborhood) - 1:
        current_index = 0

    if neighborhood[current_index] <= 0:
        print(f"Place {current_index} already had Valentine's day.")
        continue

    neighborhood[current_index] -= 2

    if neighborhood[current_index] <= 0:
        print(f"Place {current_index} has Valentine's day.")


print(f"Cupid's last position was {current_index}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len([i for i in neighborhood if i != 0])} places.")
