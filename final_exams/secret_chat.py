def insert_space(string: str, *args: str) -> str:
    index = int(args[0])
    character = " "

    string = string[:index] + character + string[index:]
    print(string)

    return string


def reverse_massage(string: str, *args: str) -> str:
    substring = ''.join(args)

    if substring in string:
        start = string.find(substring)
        end = start + len(substring)
        string = string[:start] + string[end:] + substring[::-1]
        print(string)
    else:
        print("error")

    return string


def change_all(string: str, *args: str) -> str:
    substring = args[0]
    replacement = args[1]
    string = string.replace(substring, replacement)
    print(string)

    return string


massage = input()

COMMANDS = {
    "InsertSpace": insert_space,
    "Reverse": reverse_massage,
    "ChangeAll": change_all,
}

while True:

    data = input()
    if data == "Reveal":
        print(
            f"You have a new text message: {massage}"
        )
        break

    data = data.split(":|:")
    command = data.pop(0)

    massage = COMMANDS[command](massage, *data)
