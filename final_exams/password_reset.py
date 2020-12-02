def take_odd(string: str) -> str:
    return ''.join(
        [e for i, e in enumerate(string) if i % 2 != 0]
    )


def cut(string: str, *args) -> str:
    index, length = int(args[1]), int(args[2])
    start = index
    end = index + length

    return string[:start] + string[end:]


def substitute(string: str, *args) -> str:
    substring = args[1]
    replace_string = args[2]

    if substring in string:
        string = string.replace(substring, replace_string)
        print(string)
        return string
    else:
        print("Nothing to replace!")
        return string


index = 0
raw_string = None
while True:

    data = input()
    if data == "Done":
        print(
            f"Your password is: {raw_string}"
        )
        break

    index += 1

    if index == 1:
        raw_string = data
        continue

    data = data.split()
    name = data[0]

    if name == "TakeOdd":
        raw_string = take_odd(raw_string)
        print(raw_string)

    elif name == "Cut":
        raw_string = cut(raw_string, *data)
        print(raw_string)

    elif name == "Substitute":
        raw_string = substitute(raw_string, *data)
