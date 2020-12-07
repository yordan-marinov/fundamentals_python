import re

regex = r"(@#+)([A-Z][a-zA-Z0-9]{4,}[A-Z])(@#+)"

count_of_barcodes = int(input())

for _ in range(count_of_barcodes):
    data = input()
    matched = re.findall(regex, data)
    if not matched:
        print("Invalid barcode")
        continue

    result = ""
    for c in matched[0][1]:
        if c.isdigit():
            result += c

    if not result:
        result = "00"

    print(f"Product group: {result}")
