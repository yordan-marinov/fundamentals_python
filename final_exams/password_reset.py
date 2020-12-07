def get_data_print_final_result() -> print:
    text = input()

    while True:

        data = input()
        if data == "Done":
            print(f"Your password is: {text}")
            break

        data = data.split()

        command = data.pop(0)

        text = COMMANDS[command](text, *data)


def take_odd(string: str) -> str:
    result = ""
    for character_index in range(1, len(string), 2):
        result += string[character_index]

    print(result)

    return result


def cut(string: str, *args) -> str:
    start_index = int(args[0])
    substring_length = int(args[1])
    end_index = start_index + substring_length

    string = string.replace(string[start_index: end_index], "", 1)

    print(string)

    return string


def substitute(string: str, *args) -> str:
    substring, new_substring = args[0], args[1]

    if substring in string:
        string = string.replace(substring, new_substring)
        print(string)
    else:
        print("Nothing to replace!")

    return string


COMMANDS = {
    "TakeOdd": take_odd,
    "Cut": cut,
    "Substitute": substitute,
}

get_data_print_final_result()
