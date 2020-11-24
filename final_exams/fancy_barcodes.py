def is_valid(string: str) -> str:
    if (
            string[0] == SEARCHED_SYMBOLS[0] and
            string[1] == SEARCHED_SYMBOLS[1]
    ):

        string = ''.join(
            [
                element
                for element in string
                if element not in SEARCHED_SYMBOLS
            ]
        )

        if (
                (len(string) >= 6) and
                (string.isalnum()) and
                (string[0].isupper()) and
                (string[-1].isupper())
        ):
            return string


def get_group(string: str) -> str:
    return ''.join(
        [
            element
            for element in string
            if element.isdigit()
        ]
    )


barcodes_count = int(input())

SEARCHED_SYMBOLS = "@#"

for _ in range(barcodes_count):
    barcode = input()

    if is_valid(barcode):
        if get_group(is_valid(barcode)):
            group = get_group(is_valid(barcode))
        else:
            group = "00"

        print(f"Product group: {group}")

    else:
        print("Invalid barcode")
