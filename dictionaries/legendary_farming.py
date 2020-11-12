from collections import defaultdict


def all_materials_constructor():
    key_materials = {k: 0 for k in LEGENDARY_ITEMS}
    junk_materials = defaultdict(int)

    while True:
        line = input().lower().split()

        current_value = 0
        for material in line:
            if material.isdigit():
                current_value = int(material)
                continue

            if material in LEGENDARY_ITEMS:
                key_materials[material] += current_value
                if key_materials[material] >= REQUIRED_QUANTITY:
                    return (
                        key_materials,
                        junk_materials,
                        material
                    )
            else:
                junk_materials[material] += current_value


def legendary_farming():
    (
        materials,
        non_key_materials,
        key_material
    ) = all_materials_constructor()

    print(f"{LEGENDARY_ITEMS[key_material]} obtained!")

    materials[key_material] -= REQUIRED_QUANTITY
    sorted_materials = dict(
        sorted(
            materials.items(), key=lambda p: (-p[1], p[0])
        )
    )

    [print(f"{k}: {v}") for k, v in sorted_materials.items()]
    [print(f"{k}: {v}") for k, v in sorted(non_key_materials.items())]


LEGENDARY_ITEMS = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath",
}

REQUIRED_QUANTITY = 250

legendary_farming()
