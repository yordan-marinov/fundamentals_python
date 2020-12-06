from functools import reduce
import re


def cool_threshold_number(string: str) -> int:
    matched = [int(digit) for digit in re.findall(r"\d", string)]

    return reduce(lambda x, y: x * y, matched)


def emoji_ascii_value(string: str) -> int:
    return sum([ord(letter) for letter in string])


def cool_emojis_detector_print(line: str) -> print:
    cool_threshold = cool_threshold_number(line)

    regex = r"(::|\*\*)([A-Z][a-z]{2,})\1"

    print(f"Cool threshold: {cool_threshold}")

    print(
        f"{len(re.findall(regex, line))} emojis found in the text. "
        f"The cool ones are:"
    )

    for emoji in re.finditer(regex, line):
        if emoji_ascii_value(emoji.group(2)) > cool_threshold:
            print(emoji.group())


cool_emojis_detector_print(input())
