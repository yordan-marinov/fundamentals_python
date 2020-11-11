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
        k: average_grade(v)
        for k, v in students.items()
        if average_grade(v) >= MINIMUM_GRADE
    }


MINIMUM_GRADE = 4.50

sorted_students = dict(
    sorted(get_data().items(), key=lambda p: -p[1])
)

[
    print(f"{name} -> {value:.2f}")
    for name, value in sorted_students.items()
]
