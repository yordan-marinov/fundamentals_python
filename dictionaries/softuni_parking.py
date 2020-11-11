commands_count = int(input())

parking_lot = {}

for _ in range(commands_count):
    data = input().split()

    command = data.pop(0)
    username = data[0]
    if command == "register":
        plate_number = data[1]

        if username in parking_lot:
            print(
                f"ERROR: "
                f"already registered with plate number "
                f"{parking_lot[username]}"
            )
        else:
            parking_lot[username] = plate_number
            print(
                f"{username} registered "
                f"{plate_number} successfully"
            )

    elif command == "unregister":
        if username in parking_lot:
            print(f"{username} unregistered successfully")
            del parking_lot[username]

        else:
            print(f"ERROR: user {username} not found")

[print(f"{name} => {plate}") for name, plate in parking_lot.items()]