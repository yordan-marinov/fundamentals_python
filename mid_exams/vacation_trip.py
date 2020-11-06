days_trip = int(input())
budget = float(input())
people = int(input())
fuel_km = float(input())
food_person = float(input())
room_person = float(input())


food_group = food_person * people * days_trip
hotel_group = room_person * people * days_trip

if people > 10:
    hotel_group *= 0.75

current_expenses = food_group + hotel_group
flag = True
for day in range(1, days_trip + 1):

    distance = float(input())
    travel_expenses = distance * fuel_km
    current_expenses += travel_expenses

    if day % 3 == 0 or day % 5 == 0:
        current_expenses *= 1.40

    if day % 7 == 0:
        money = current_expenses / people
        current_expenses -= money

    if current_expenses > budget:
        flag = False
        break

if flag:
    print(
        f"You have reached the destination. "
        f"You have {budget - current_expenses:.2f}$ budget left."
    )
else:
    print(
        f"Not enough money to continue the trip. "
        f"You need {current_expenses - budget:.2f}$ more."
    )