from functools import reduce


def remove_surround_symbols(string: str) -> str:
    return string[2:-2]


def valid_emojis(string: str) -> list:
    valid = []
    for item in string.split():
        if (
                (item[:VALID_SURROUND_SYMBOLS[":"]] == item[-VALID_SURROUND_SYMBOLS[":"]:]) or
                (item[:VALID_SURROUND_SYMBOLS["*"] == item[-VALID_SURROUND_SYMBOLS["*"]:]])
        ):

            if (
                    (len(item[2:-2]) >= MINIMUM_EMOJI_LENGTH) and
                    (item[2:-2][0].isupper()) and
                    (item[2:-2][1:].islower())
            ):
                valid.append(item)

    return valid


strings = input()

VALID_SURROUND_SYMBOLS = {
    ":": 2,
    "*": 2,
}
MINIMUM_EMOJI_LENGTH = 3

cool_threshold = reduce(
    lambda x, y: x * y, [int(n) for n in strings if n.isdigit()]
)

print(f"Cool threshold: {cool_threshold}")
print(
    f"{len(valid_emojis(strings))} emojis found in the text. "
    f"The coll ones are:"
)

emoji_values = []
for emoji in valid_emojis(strings):

    result = 0
    for letter in emoji:
        if letter not in VALID_SURROUND_SYMBOLS:
            result += ord(letter)

    if result >= cool_threshold:
        print(f"{emoji}")