def contains(lst: list, substring: str) -> list:
    if substring in ''.join(lst):
        print(f"{''.join(lst)} contains {substring}")
    else:
        print("Substring not found!")

    return lst


def flip(lst: list, subcommand: str, start: str, end: str) -> list:
    start_index, end_index = int(start), int(end)

    result = []
    for i, e in enumerate(lst):

        if i in range(start_index, end_index):
            if subcommand == "Upper":
                result.append(e.upper())
            else:
                result.append(e.lower())
        else:
            result.append(e)

    print(''.join(result))

    return result


def slice(lst: list, start: str, end: str) -> list:
    start_index, end_index = int(start), int(end)
    result = [
        e
        for i, e in enumerate(lst)
        if i not in range(start_index, end_index)
    ]

    print(''.join(result))

    return result


raw_activation_key = [l for l in input()]

while True:

    data = input()
    if data == "Generate":
        print(
            f"Your activation key is: {''.join(raw_activation_key)}"
        )
        break

    data = data.split(">>>")
    command = data.pop(0)

    if command == "Contains":
        raw_activation_key = contains(raw_activation_key, *data)

    elif command == "Flip":
        raw_activation_key = flip(raw_activation_key, *data)

    elif command == "Slice":
        raw_activation_key = slice(raw_activation_key, *data)
