from collections import defaultdict


def average_grade(lst):
    return sum(lst) / len(lst)


def get_data():
    count = int(input())

    students = defaultdict(list)
    for _ in range(count):
        name = input()
        grade = float(input())
        students[name].append(grade)

    return {
        key: average_grade(value)
        for key, value in students.items()
        if average_grade(value) >= MINIMUM_GRADE
    }


MINIMUM_GRADE = 4.50

sorted_students = dict(
    sorted(
        get_data().items(),
        key=lambda p: -p[1]
    )
)

[
    print(f"{name} -> {value:.2f}")
    for name, value in sorted_students.items()
]
