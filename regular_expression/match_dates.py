import re

data = input()
regex = r"\b(?P<day>\d{2})(?P<separator>[-\./])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"

matched = re.findall(regex, data)

[
    print(
        f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}"
    )
    for match in matched
]
