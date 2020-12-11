def insert_space(string: str, *args) -> str:
    index = int(args[0])

    string = string[:index] + " " + string[index:]
    print(string)

    return string


def reverse_string(string: str, *args) -> str:
    substring = args[0]

    if substring not in string:
        print("error")
        return string

    string = string.replace(substring, "", 1)
    string = string + substring[::-1]
    print(string)

    return string


def change_all(string: str, *args) -> str:
    substring, new_substring = args

    string = string.replace(substring, new_substring)
    print(string)

    return string


def main_manipulation_print_func(commands: dict) -> print:
    concealed_message = input()

    while True:
        data = input()
        if data == "Reveal":
            print(f"You have a new text message: {concealed_message}")
            break

        data = data.split(":|:")
        command = data.pop(0)

        concealed_message = commands[command](concealed_message, *data)


COMMANDS = dict(InsertSpace=insert_space, Reverse=reverse_string, ChangeAll=change_all)


main_manipulation_print_func(COMMANDS)
