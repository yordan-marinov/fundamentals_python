from collections import defaultdict


def get_submissions(dd: dict) -> dict:
    result = defaultdict(lambda: defaultdict(int))
    while True:

        data = input()
        if data == "end of submissions":
            break

        data = data.split("=>")
        contest = data[0]
        password = data[1]
        username = data[2]
        points = int(data[3])

        if contest in dd and dd[contest] == password:
            if contest not in result[username]:
                result[username][contest] = points

            if points > result[username][contest]:
                result[username][contest] = points

    return result


def print_statement(dd: dict) -> print:
    best_student = None
    max_result = 0
    for name, subjects in dd.items():

        current_result = 0
        for subject, points in subjects.items():
            current_result += points

        if current_result > max_result:
            max_result = current_result
            best_student = name

    print(
        f"Best candidate is {best_student} "
        f"with total {max_result} points."
    )

    print("Ranking:")
    for student, values in sorted(dd.items()):
        print(student)
        for contest, value in sorted(
                values.items(), key=lambda a: -a[1]
        ):
            print(f"#  {contest} -> {value}")


contests = {}
while True:

    token = input()
    if token == "end of contests":
        break

    token = token.split(":")
    contest_data = token[0]
    password_data = token[1]

    contests[contest_data] = password_data

submissions = get_submissions(contests)
print_statement(submissions)
