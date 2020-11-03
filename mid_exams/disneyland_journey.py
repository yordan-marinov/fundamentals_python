journey_cost = int(input())
months = int(input())

monthly_savings = journey_cost * 0.25


saved_money = 0
for month in range(1, months + 1):

    if month % 2 != 0 and month != 1:
        saved_money *= 0.84

    if month % 4 == 0:
        saved_money *= 1.25


    saved_money += monthly_savings


if saved_money >= journey_cost:
    print(
        f"Bravo! You can go to Disneyland and "
        f"you will have {saved_money - journey_cost:.2f}lv. "
        f"for souvenirs."
    )

else:
    print(f"Sorry. You need {journey_cost - saved_money:.2f}lv. more.")