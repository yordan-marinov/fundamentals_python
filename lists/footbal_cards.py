team_number = input().split()

a_team = [str(i) for i in range(1, 12)]
b_team = [str(i) for i in range(1, 12)]

is_terminated = False
for pair in team_number:
    team, number = pair.split("-")

    if team == "A" and number in a_team:
        a_team.remove(number)

    elif team == "B" and number in b_team:
        b_team.remove(number)

    if (
        (len(a_team) < 7) or
        (len(b_team) < 7)
    ):
        is_terminated = True
        break

print(f"Team A - {len(a_team)}; Team B - {len(b_team)}")
if is_terminated:
    print("Game was terminated")
