targets = list(map(int, input().split('|')))
text = input().split('@')
points = 0

while text[0] != 'Game over':
    command = text[0]
    if command == 'Shoot Left':
        start_index = int(text[1])
        length = int(text[2])
        if 0 <= start_index < len(targets):
            if (start_index - length) < 0:
                current_index = (start_index - length) % len(targets)
            else:
                current_index = start_index - length
            if targets[current_index] >= 5:
                targets[current_index] -= 5
                points += 5
            elif 0 < targets[current_index] < 5:
                points += targets[current_index]
                targets[current_index] = 0
    elif command == 'Shoot Right':
        start_index = int(text[1])
        length = int(text[2])
        if 0 <= start_index < len(targets):
            if start_index + length > len(targets):
                current_index = (start_index + length) % len(targets)
            else:
                current_index = start_index + length
            if targets[current_index] >= 5:
                targets[current_index] -= 5
                points += 5
            elif 0 < targets[current_index] < 5:
                points += targets[current_index]
                targets[current_index] = 0
    elif command == 'Reverse':
        targets = targets[:: -1]
    text = input().split('@')
print(' - '.join(str(i) for i in targets))
print(f'Iskren finished the archery tournament with {points} points!')