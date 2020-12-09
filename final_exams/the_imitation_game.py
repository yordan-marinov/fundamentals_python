def move(string: str, *args) -> str:
    number_of_letters = int(args[0])

    string = string[number_of_letters:] + string[: number_of_letters]
    return string


def insert(string: str, *args) -> str:
    index = int(args[0])
    value = args[1]

    string = string[:index] + value + string[index:]
    return string


def change_all(string: str, *args) -> str:
    substring = args[0]
    new_substring = args[1]

    string = string.replace(substring, new_substring)

    return string


def main_manipulation_printing_func(string: str, commands: dict) -> print:
    while True:

        data = input()
        if data == "Decode":
            print(f"The decrypted message is: {string}")
            break

        data = data.split("|")
        command = data.pop(0)

        string = commands[command](string, *data)


COMMANDS = dict(Move=move, Insert=insert, ChangeAll=change_all)

encrypted_message = input()
main_manipulation_printing_func(encrypted_message, COMMANDS)