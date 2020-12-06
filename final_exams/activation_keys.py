def main(string: str) -> str:
    while True:

        data = input()
        if data == "Generate":
            print(f"Your activation key is: {string}")
            break

        data = data.split(">>>")
        command = data.pop(0)

        string = COMMANDS[command](string, *data)

    return string


def contains(string: str, *args) -> str:
    substring = args[0]
    if substring not in string:
        print("Substring not found!")
    else:
        print(f"{string} contains {substring}")

    return string


def flip(string: str, *args) -> str:
    start_index = int(args[1])
    end_index = int(args[2])

    if args[0] == "Upper":
        string = string.replace(
            string[start_index: end_index],
            string[start_index: end_index].upper()
        )
    else:
        string = string.replace(
            string[start_index: end_index],
            string[start_index: end_index].lower()
        )

    print(string)
    return string


def slice_string(string: str, *args) -> str:
    start_index = int(args[0])
    end_index = int(args[1])

    string = string.replace(
        string[start_index: end_index], ""
    )
    print(string)
    return string


COMMANDS = {
    "Contains": contains,
    "Flip": flip,
    "Slice": slice_string,
}

raw_activation_key = input()
main(raw_activation_key)
