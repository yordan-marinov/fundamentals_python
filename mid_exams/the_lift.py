def lift_order(people, runs):
    que = people

    for index in range(len(runs)):
        current_run = LIFT_MAXIMUM_PEOPLE - runs[index]

        if que < current_run:
            current_run = que

        que -= current_run
        runs[index] += current_run

    return que, runs


LIFT_MAXIMUM_PEOPLE = 4

waiting_people = int(input())
lift_runs = [int(p) for p in input().split()]

left_people, lift = lift_order(waiting_people, lift_runs)

is_full = (
        LIFT_MAXIMUM_PEOPLE * len(lift) == sum(lift)
)

if left_people == 0 and not is_full:
    print("The lift has empty spots!")
    print(" ".join(str(e) for e in lift_runs))

elif left_people > 0 and is_full:
    print(
        f"There isn't enough space! "
        f"{left_people} people in a queue!"
    )
    print(" ".join(str(e) for e in lift_runs))

else:
    print(" ".join(str(e) for e in lift_runs))
