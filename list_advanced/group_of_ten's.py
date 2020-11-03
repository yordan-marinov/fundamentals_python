from math import ceil


def groups_creator(lst, length_of_group):
    groups_count = ceil(max(lst) / length_of_group)

    for i in range(1, groups_count + 1):
        group_end = i * length_of_group
        group_start = group_end - length_of_group

        current_group = [
            number for number in lst
            if group_start < number <= group_end
        ]

        print(f"Group of {group_end}'s: {current_group}")


numbers = [int(e) for e in input().split(", ")]

GROUP_LENGTH = 10

groups_creator(numbers, GROUP_LENGTH)
