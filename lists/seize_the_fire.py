fires = input().split("#")
water_liters = int(input())

effort = 0
total_fire = 0

print("Cells:")

for fire in fires:

    type_fire, level_fire = fire.split(" = ")
    level_fire = int(level_fire)
    if level_fire > water_liters:
        continue

    is_valid = (
            (type_fire == "High" and 81 <= level_fire <= 125) or
            (type_fire == "Medium" and 51 <= level_fire <= 80) or
            (type_fire == "Low" and 1 <= level_fire <= 50)
    )

    if is_valid:
        water_liters -= level_fire
        effort += level_fire / 4
        total_fire += level_fire
        print(f"- {level_fire}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
