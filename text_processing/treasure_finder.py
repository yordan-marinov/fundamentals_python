def data_extractor(string: str, splitters: tuple) -> str:
    splitter_1, splitter_2 = splitters
    string = string.split(splitter_1, 1)
    string = string[1].split(splitter_2, 1)
    return string[0]


keys = [int(b) for b in input().split()]

TYPE_SEPARATORS = ("&", "&")
COORDINATES_SEPARATOR = ("<", ">")

while True: 

    line = input()
    if line == "find":
        break

    keys_copy = keys.copy()
    result = ""
    for symbol in line:
        result += chr(ord(symbol) - keys_copy[0])
        keys_copy.append(keys_copy.pop(0))

    treasure_type = data_extractor(result, TYPE_SEPARATORS)
    treasure_coordinates = data_extractor(result, COORDINATES_SEPARATOR)

    print(f"Found {treasure_type} at {treasure_coordinates}")
