def add_stop(line: str, *args) -> str:
    index = int(args[0])
    destination = args[1]

    if index in range(len(line)):
        line = line[:index] + destination + line[index:]

    return line


def remove_stop(line: str, *args) -> str:
    start_index = int(args[0])
    end_index = int(args[1])

    if (
            start_index in range(len(line)) and
            end_index in range(len(line))
    ):
        line = line[:start_index] + line[end_index + 1:]

    return line


def switch(line: str, *args) -> str:
    old_part = args[0]
    new_part = args[1]

    if old_part in line:
        line = line.replace(old_part, new_part)

    return line


string = input()

COMMANDS = {
    "Add Stop": add_stop,
    "Remove Stop": remove_stop,
    "Switch": switch,
}

while True:

    data = input()
    if data == "Travel":
        print(
            f"Ready for world tour! "
            f"Planned stops: {string}"
        )
        break

    data = data.split(":")
    command = data.pop(0)

    string = COMMANDS[command](string, *data)

    print(string)
