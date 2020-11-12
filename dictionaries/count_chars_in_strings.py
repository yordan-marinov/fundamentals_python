string = input()

characters_count = {}
for character in string:
    if not character == " ":
        characters_count[character] = characters_count.get(character, 0) + 1

[print(f"{k} -> {v}") for k, v in characters_count.items()]
