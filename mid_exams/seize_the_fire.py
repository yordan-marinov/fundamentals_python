fire_cells = input().split("#")
water = int(input())

HIGH = range(81, 126)
MEDIUM = range(51, 81)
LOW = range(1, 51)

effort = 0
total_fire = 0

print("Cells:")
for fire_cell in fire_cells:
    fire_cell = fire_cell.split(" = ")
    fie_types = fire_cell[0]
    fire_value = int(fire_cell[1])

    if fie_types == "High" and fire_value in HIGH:
        if water >= fire_value:
            effort += (fire_value * 0.25)
            water -= fire_value
            total_fire += fire_value
            print(f"- {fire_value}")

    elif fie_types == "Medium" and fire_value in MEDIUM:
        if water >= fire_value:
            effort += (fire_value * 0.25)
            water -= fire_value
            total_fire += fire_value
            print(f"- {fire_value}")

    elif fie_types == "Low" and fire_value in LOW:
        if water >= fire_value:
            effort += (fire_value * 0.25)
            water -= fire_value
            total_fire += fire_value
            print(f"- {fire_value}")


print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")