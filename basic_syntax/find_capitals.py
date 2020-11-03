string = input()

indexes = []
for index, character in enumerate(string):
    is_true = character.isupper()
    if is_true:
        indexes.append(index)

print(indexes)
