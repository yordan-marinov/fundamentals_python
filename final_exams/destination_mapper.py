import re

regex = r"(/|=)([A-Z][A-Za-z]{2,})\1"

matched = [
    match.group(2)
    for match in re.finditer(regex, input())
]

print(f"Destinations: {', '.join(matched)}")
print(f"Travel Points: {sum([len(l) for l in matched])}")
