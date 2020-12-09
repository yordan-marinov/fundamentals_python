import re

CALORIES_A_DAY = 2_000

regex = r"(#|\|)([a-zA-Z\s]+)\1(\d{2}/\d{2}/\d{2})\1([0-9][0-9]{,3}|10000)\1"

text_string = input()

matched = re.findall(regex, text_string)

total_calories = sum(int(product[3]) for product in matched)

print(
    f"You have food to last you for: "
    f"{total_calories // CALORIES_A_DAY} days!"
)

for product in matched:
    print(
        f"Item: {product[1]}, "
        f"Best before: {product[2]}, "
        f"Nutrition: {product[3]}"
    )
