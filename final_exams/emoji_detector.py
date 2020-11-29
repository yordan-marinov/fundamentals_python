from functools import reduce
import re


def cool_threshold(string: str) -> int:
    return reduce(
        lambda x, y: x * y,
        [
            int(number)
            for number in string
            if number.isdigit()
        ]
    )


def get_matched(pattern: str, string: str) -> dict:
    return {
        match.group(): sum(
            [ord(character) for character in match.group(2)
             if character not in SURROUNDED_SYMBOLS]
        )
        for match in re.finditer(pattern, string)
    }


def print_statement(string: str, matched_dict: dict) -> print:
    print(f"Cool threshold: {cool_threshold(string)}")

    print(
        f"{len(matched_dict)} emojis found in the text. "
        f"The cool ones are:"
    )
    [
        print(emoji)
        for emoji, value in matched_dict.items()
        if value >= cool_threshold(string)
    ]


SURROUNDED_SYMBOLS = (":", "*")

strings = input()

regex = r"(\*\*|::)([A-Z][a-z][a-z]+)\1"
matched = get_matched(regex, strings)

print_statement(strings, matched)
