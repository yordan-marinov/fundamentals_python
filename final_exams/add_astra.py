import re

DAY_CALORIES = 2000
regex = r"(#|\|)([a-zA-Z ]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"

text = input()

total_calories = sum(
    [
        int(calorie.group(4))
        for calorie in re.finditer(regex, text)
    ]
)
days = total_calories // DAY_CALORIES

print(f"You have food to last you for: {days} days!")
for match in re.finditer(regex, text):
    print(
        f"Item: {match.group(2)}, "
        f"Best before: {match.group(3)}, "
        f"Nutrition: {match.group(4)}"
    )
