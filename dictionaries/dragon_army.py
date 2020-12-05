from collections import defaultdict


def get_dragons_data() -> dict:
    dragons_count = int(input())

    dragons_data = {}
    for _ in range(dragons_count):

        data = input().split()
        type = data.pop(0)
        name = data.pop(0)

        key = (type, name)
        values = {}
        for index, value in enumerate(data):
            if value == "null":
                values[DEFAULT_VALUES[index][0]] = DEFAULT_VALUES[index][1]
            else:
                values[DEFAULT_VALUES[index][0]] = int(value)

        dragons_data[key] = values

    return dragons_data


def average_values(*args, count: int):
    for arg in  args:




DEFAULT_VALUES = {
    0: ("damage", 45),
    1: ("health", 250),
    2: ("armor", 10),
}

# }
dragons = get_dragons_data()

types = defaultdict(list)
for k, v in dragons.items():
    key = k[0]
    value = {k[1]: [i for i in v.values()]}
    types[key].append(value)

print(types)

for t, name in types.items():
    average_damage, average_health, average_armor = average_values(*name.values(), len(name))
    print(f"{t}::({average_damage}/{average_health}/{average_armor})")
