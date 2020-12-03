from collections import defaultdict


def get_data() -> tuple:
    users_data = defaultdict(lambda: defaultdict(int))
    contests_data = defaultdict(lambda: defaultdict(int))

    while True:

        data = input()
        if data == "no more time":
            break

        data = data.split(" -> ")
        username = data[0]
        contest = data[1]
        points = int(data[2])

        if points > users_data[username][contest]:
            users_data[username][contest] = points
            contests_data[contest][username] = points

    return users_data, contests_data


def users_total_points(dd: dict) -> dict:
    total_points = {}
    for name, values in dd.items():

        currant_points = 0
        for k, v in values.items():
            currant_points += v

        total_points[name] = currant_points

    return total_points


def print_statement(func) -> print:
    users, contests = func()
    for contest, values in contests.items():
        print(f"{contest}: {len(values)} participants")
        position = 0
        for key, value in sorted(values.items(), key=lambda a: (-a[1], a[0])):
            position += 1
            print(f"{position}. {key} <::> {value}")

    print("Individual standings:")

    positions = 0
    for name, points in sorted(
            users_total_points(users).items(),
            key=lambda x: (-x[1], x[0])
    ):
        positions += 1
        print(f"{positions}. {name} -> {points}")


print_statement(get_data)
