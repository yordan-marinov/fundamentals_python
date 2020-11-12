from collections import defaultdict


def data_sides_users():
    force_sides = defaultdict(list)

    while True:

        data = input()
        if data == "Lumpawaroo":
            return {
                key: sorted(value)
                for key, value in force_sides.items()
                if value
            }

        if "|" in data:
            side, user = data.split(" | ")

            if user not in force_sides[side]:
                force_sides[side].append(user)

        else:
            user, side = data.split(" -> ")
            for users_list in force_sides.values():
                for every_user in users_list:

                    if user in every_user:
                        users_list.remove(user)
                        break

            force_sides[side].append(user)
            print(f"{user} joins the {side} side!")


sorted_sides = dict(
    sorted(
        data_sides_users().items(),
        key=lambda x: (-len(x[1]), x[0])
    )
)

for side, users in sorted_sides.items():
    print(f"Side: {side}, Members: {len(users)}")
    # [print(f"! {value}") for value in users]
    for value in users:
        print(f"! {value}")
