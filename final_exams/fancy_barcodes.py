import re

regex = r"(@#+)([A-Z][a-zA-Z0-9]{4,}[A-Z])(@#+)"

count_of_barcodes = int(input())
for _ in range(count_of_barcodes):
    matched = re.match(regex, input())
    if not matched:
        print("Invalid barcode")
    else:
        match = re.findall(r"\d", matched.group(2))
        if not match:
            match = '00'
        else:
            match = "".join(match)

        print(f"Product group: {match}")