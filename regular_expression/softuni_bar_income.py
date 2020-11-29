import re

regex = r"(^|(?<=%))([A-Z][a-z]+)(%)(<)([A-z][a-z]+)(>)(\|)(\d+)\7(\d+.\d+)((?=\$)|$)"
total = 0
while True:

    data = input()
    if data == "end of shift":
        print(f"Total income: {total:.2f}")
        break

    matched = re.finditer(regex, data)

    for m in matched:
        result = float(m.group(8)) * float(m.group(9))
        total += result
        print(
            f"{m.group(2)}: {m.group(5)} - {result}"
        )

