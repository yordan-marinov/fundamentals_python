fire_cells = input().split("#")
water = int(input())

HIGH = range(81, 126)
MEDIUM = range(51, 81)
LOW = range(1, 51)

print("Cells:")
total_fire = 0
effort = 0
for fire_cell in fire_cells:

    level, token = fire_cell.split(" = ")
    value = int(token)

    if water >= value and (
            (level == "High" and value in HIGH) or
            (level == "Medium" and value in MEDIUM) or
            (level == "Low" and value in LOW)
    ):
        total_fire += value
        water -= value
        current_effort = value * 0.25
        effort += current_effort
        print(f"- {value}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
