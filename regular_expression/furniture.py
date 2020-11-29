# from collections import defaultdict
import re

# bought_furniture = defaultdict(float)
items = []
price = 0
while True:

    data = input()
    if data == "Purchase":

        print(f"Bought furniture:")

        for name in items:
            print(name)

        print(
            f"Total money spend: "
            f"{price:.2f}"
        )

        break

    regex = r"^>{2}([A-Za-z]+)<{2}(\d+(\.\d+)?)!(\d+)"

    furniture = re.finditer(regex, data)

    for item in furniture:
        value = float(item.group(2)) * float(item.group(4))
        # bought_furniture[item.group(1)] += value
        price += value
        items.append(item.group(1))