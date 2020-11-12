from collections import defaultdict


def sorting_dicts(dct):
    return dict(
            sorted(
                dct.items(), key=lambda x: (-x[1], x[0])
            )
        )


def printing(dct, separator="|"):
    [
        print(f"{name} {separator} {values}")
        for name, values in sorting_dicts(dct).items()
    ]


results = defaultdict(int)
submissions = defaultdict(int)

while True:

    data = input()
    if data == "exam finished":
        print("Results:")
        printing(results)
        print("Submissions:")
        printing(submissions, separator="-")
        break

    token = data.split("-")
    username = token[0]

    if token[1] == "banned":
        del results[username]

    else:
        language, points = token[1], int(token[2])

        if points > results[username]:
            results[username] = points

        submissions[language] += 1
