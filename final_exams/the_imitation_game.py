def main_manipulation_print_func(string: str, commands) -> print:
    while True:
        data = input()
        if data == "Decode":
            print(f"The decrypted message is: {string}")
            break

        data = data.split("|")
        command = data.pop(0)

        string = commands[command](string, *data)


def move(string: str, *args) -> str:
    number_of_letters = int(args[0])

    substring = string[:number_of_letters]
    string = string.replace(substring, "")
    string += substring

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


COMMANDS = dict(Move=move, Insert=insert, ChangeAll=change_all)

encrypted_message = input()
main_manipulation_print_func(encrypted_message, COMMANDS)
