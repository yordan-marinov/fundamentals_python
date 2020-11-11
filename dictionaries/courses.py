from collections import defaultdict


def courses_registration():
    result = defaultdict(list)
    while True:

        data = input()
        if data == "end":
            return result

        course, user = data.split(" : ")

        result[course].append(user)


courses = dict(
    sorted(
        courses_registration().items(),
        key=lambda a: -len(a[1])
    )
)

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for name in sorted(value):
        print(f"-- {name}")
