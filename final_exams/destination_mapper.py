import re

regex = r"(\/|=)([A-Z][a-zA-Z]{2,})\1"

string = input()

matched = {
    match.group(2): len(match.group(2))
    for match in re.finditer(regex, string)
}

print(f"Destinations: {', '.join(matched.keys())}")
print(f"Travel Points: {sum(matched.values())}")
