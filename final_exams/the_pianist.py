def get_data(n: int) -> dict:
    result = {}
    for _ in range(n):
        data = input().split("|")
        piece = data[0]
        composer = data[1]
        key = data[2]

        result[piece] = {"composer": composer, "key": key}

    return result


def add_elements(dd: dict, *args) -> dict:
    piece, composer, key = args

    if piece in dd:
        print(
            f"{piece} is already in the collection!"
        )
        return dd

    dd[piece] = {"composer": composer, "key": key}
    print(
        f"{piece} by {composer} in {key} "
        f"added to the collection!"
    )

    return dd


def remove_elements(dd: dict, *args) -> dict:
    piece = args[0]

    if piece in dd:
        print(f"Successfully removed {piece}!")
        del dd[piece]

    else:
        print(
            f"Invalid operation! {piece} "
            f"does not exist in the collection."
        )

    return dd


def change_key(dd: dict, *args) -> dict:
    piece, new_key = args

    if piece in dd:
        print(f"Changed the key of {piece} to {new_key}!")
        dd[piece]["key"] = new_key

    else:
        print(
            f"Invalid operation! "
            f"{piece} does not exist in the collection."
        )

    return dd


def main(dd: dict):
    while True:

        data = input()
        if data == "Stop":
            print_statement(dd)
            break

        data = data.split("|")
        command = data.pop(0)

        COMMANDS[command](dd, *data)


def print_statement(dd: dict) -> print:
    for name_piece, values in sorted(
            dd.items(),
            key=lambda x: (x[0], x[1]["composer"])
    ):
        print(f"{name_piece} -> Composer: {values['composer']}, Key: {values['key']}")


COMMANDS = {
    "Add": add_elements,
    "Remove": remove_elements,
    "ChangeKey": change_key,
}

count = int(input())
pieces: dict = get_data(count)
main(pieces)
