def shoot_targets(lst, start, radius):
    end_index = None
    if command == "Shoot Left":
        end_index = (start - radius) % len(lst)

    elif command == "Shoot Right":
        end_index = (start + radius) % len(lst)

    if lst[end_index] > 5:
        p = 5
        lst[end_index] -= 5
    else:
        p = lst[end_index]
        lst[end_index] = 0

    return lst, p


targets = [int(n) for n in input().split("|")]

points = 0
while True:

    data = input()
    if data == "Game over":
        print(" - ".join(str(t) for t in targets))
        print(
            f"Iskren finished the archery tournament "
            f"with {points} points!"
        )
        break

    elif data == "Reverse":
        targets = targets[::-1]
        continue

    command, *token = data.split("@")
    start_index, length = [int(i) for i in token]

    if start_index in range(len(targets)):
        targets, current_points = shoot_targets(
            targets, start_index, length
        )

        points += current_points
