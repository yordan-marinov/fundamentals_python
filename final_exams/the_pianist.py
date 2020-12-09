def get_data() -> dict:
    n = int(input())
    pieces_data = {}
    for _ in range(n):
        data = input().split("|")
        piece = data[0]
        composer = data[1]
        key = data[2]

        pieces_data[piece] = {
            "composer": composer,
            "key": key
        }
    return pieces_data


def add_data(dd: dict, *args):
    current_piece, current_composer, current_key = args

    if current_piece in dd:
        print(f"{current_piece} is already in the collection!")
    else:
        print(
            f"{current_piece} by {current_composer} in "
            f"{current_key} added to the collection!"
        )
        dd[current_piece] = {
            "composer": current_composer,
            "key": current_key
        }


def remove_data(dd: dict, *args):
    current_piece = args[0]

    if current_piece in dd:
        print(f"Successfully removed {current_piece}!")
        del dd[current_piece]
    else:
        print(
            f"Invalid operation! "
            f"{current_piece} does not exist in the collection."
        )


def change_key(dd: dict, *args):
    current_piece, new_key = args

    if current_piece in dd:
        print(f"Changed the key of {current_piece} to {new_key}!")
        dd[current_piece]["key"] = new_key
    else:
        print(
            f"Invalid operation! "
            f"{current_piece} does not exist in the collection."
        )


def sorting_printing_func(dd: dict) -> print:
    for piece, values in sorted(
            dd.items(),
            key=lambda pair: (pair[0], pair[1]["composer"])
    ):
        print(f"{piece} -> Composer: {values['composer']}, Key: {values['key']}")


def main_manipulation_print_func(dd: dict, commands) -> print:
    while True:

        data = input()
        if data == "Stop":
            sorting_printing_func(dd)
            break

        data = data.split("|")
        command = data.pop(0)

        commands[command](dd, *data)


COMMANDS = dict(Add=add_data, Remove=remove_data, ChangeKey=change_key)

pieces = get_data()
main_manipulation_print_func(pieces, COMMANDS)
