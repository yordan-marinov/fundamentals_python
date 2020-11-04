def distribution(lst, count_people, max_people):
    for index in range(len(lst)):

        current_run = max_people - lst[index]
        if count_people < current_run:
            current_run = count_people

        lst[index] += current_run
        count_people -= current_run

    return count_people, lst


def lift_distribution(max_people):
    que = int(input())
    lift = [int(n) for n in input().split()]

    que, lift = distribution(lift, que, MAXIMUM_PEOPLE)

    is_lift_full = (
            max_people * len(lift) == sum(lift)
    )

    if que == 0 and not is_lift_full:
        print(f"The lift has empty spots!")
        print(*lift)

    elif que > 0 and is_lift_full:
        print(f"There isn't enough space! {que} people in a queue!")
        print(*lift)

    elif que == 0 and is_lift_full:
        print(*lift)


MAXIMUM_PEOPLE = 4

lift_distribution(MAXIMUM_PEOPLE)
