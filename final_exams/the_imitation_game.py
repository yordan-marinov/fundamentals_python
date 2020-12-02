def move_letters(string: str, *args) -> str:
    number = int(args[0])
    substring = string[:number]

    return string[number:] + substring


def insert_letters(string: str, *args) -> str:
    index = int(args[0])
    value = args[1]

    return string[:index] + value + string[index:]


def change_all(string: str, *args) -> str:
    substring = args[0]
    replacement = args[1]

    return string.replace(substring, replacement)


encrypted_message = input()

COMMANDS = {
    "Move": move_letters,
    "Insert": insert_letters,
    "ChangeAll": change_all,
}

while True:

    data = input()
    if data == "Decode":
        print(
            f"The decrypted message is: {encrypted_message}"
        )

        break

    data = data.split("|")
    command = data.pop(0)

    encrypted_message = COMMANDS[command](encrypted_message, *data)
