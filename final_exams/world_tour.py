def add_stop(string: str, *args) -> str:
    index = int(args[0])
    substring = args[1]

    if index in range(len(string)):
        string = string[:index] + substring + string[index:]

    return string


def remove_stop(string: str, *args) -> str:
    start_index = int(args[0])
    end_index = int(args[1])

    if start_index in range(len(string)) and end_index in range(len(string)):
        string = string.replace(string[start_index:end_index + 1], "")

    return string


def switch(string: str, *args) -> str:
    substring = args[0]
    new_substring = args[1]

    string = string.replace(substring, new_substring)

    return string


def main_manipulation_print_func(string: str) -> print:
    while True:

        data = input()
        if data == "Travel":
            print(f"Ready for world tour! Planned stops: {string}")
            break

        data = data.split(":")
        command = data.pop(0)

        string = COMMANDS[command](string, *data)

        print(string)


COMMANDS = {
    "Add Stop": add_stop,
    "Remove Stop": remove_stop,
    "Switch": switch,
}

stops: str = input()
main_manipulation_print_func(stops)
