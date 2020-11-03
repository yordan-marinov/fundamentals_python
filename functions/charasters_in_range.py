def characters_in_range(char_1, char_2):
    return " ".join(
        [chr(i) for i in range(ord(char_1) + 1, ord(char_2))]
    )


first_character = input()
end_character = input()
print(characters_in_range(first_character, end_character))
