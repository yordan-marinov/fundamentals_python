targets = [int(i) for i in input().split()]

hit_counter = 0
while True:
    command = input()
    if command == "End":
        break

    target_index = int(command)
    if target_index not in range(len(targets)) or targets[target_index] == -1:
        continue

    hit_counter += 1
    hit_number = targets[target_index]

    for i in range(len(targets)):
        targets[target_index] = -1

        if targets[i] > hit_number and targets[i] != -1:
            targets[i] -= hit_number

        elif targets[i] <= hit_number and targets[i] != -1:
            targets[i] += hit_number

print(f"Shot targets: {hit_counter} -> {' '.join([str(i) for i in targets])}")
