from collections import defaultdict

dwarfs = {}

while True:

    data = input()
    if data == "Once upon a time":
        break

    data = data.split(" <:> ")
    dwarf_name = data[0]
    dwarf_hat_color_counter = data[1]
    dwarf_physics = int(data[2])

    key = (dwarf_name, dwarf_hat_color_counter)

    if key not in dwarfs or dwarfs[key] < dwarf_physics:
        dwarfs[key] = dwarf_physics

dwarf_hat_color_counter = defaultdict(int)
for key in dwarfs.keys():
    dwarf_hat_color_counter[key[1]] += 1

for keys, values in sorted(
        dwarfs.items(),
        key=lambda a: (-a[1], -dwarf_hat_color_counter[a[0][1]])
):
    print(f"({keys[1]}) {keys[0]} <-> {values}")
