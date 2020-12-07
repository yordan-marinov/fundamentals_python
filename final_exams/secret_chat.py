def insert_space(string: str, *args) -> str:
    index = int(args[0])

    string = string[:index] + " " + string[index:]
    print(string)
    return string


def reverse(string: str, *args) -> str:
    substring = args[0]

    if substring not in string:
        print("error")
    else:
        string = string.replace(substring, "", 1)
        string = string + substring[::-1]
        print(string)
    return string


def change_all(string: str, *args) -> str:
    substring = args[0]
    new_substring = args[1]

    string = string.replace(substring, new_substring)
    print(string)
    return string


def main():
    massage = input()

    while True:

        data = input()
        if data == "Reveal":
            print(f"You have a new text message: {massage}")
            break

        data = data.split(":|:")
        command = data.pop(0)

        massage = COMMANDS[command](massage, *data)


COMMANDS = {
    "InsertSpace": insert_space,
    "Reverse": reverse,
    "ChangeAll": change_all,
}

main()
