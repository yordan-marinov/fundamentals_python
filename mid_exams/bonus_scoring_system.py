from math import ceil


def total_bonus(lect_count, add_bonus, attendances):
    return attendances / lect_count * (5 + add_bonus)


students_count = int(input())
lectures_count = int(input())
bonus = int(input())

max_bonus = 0
attend = 0
for student in range(students_count):
    attendances_student = int(input())

    if lectures_count > 0:
        current_bonus = total_bonus(
            lectures_count, bonus, attendances_student
        )

        if current_bonus >= max_bonus:
            max_bonus = current_bonus
            attend = attendances_student

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {ceil(attend)} lectures.")
