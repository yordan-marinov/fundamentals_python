days = int(input())
budget = float(input())
people = int(input())
fuel_km = float(input())
food_person = float(input())
hotel_person = float(input())

food_group = days * people * food_person
hotel_group = days * people * hotel_person
if people >= 10:
    hotel_group *= 0.25


expenses = 0
flag = True
for day in range(1, days + 1):

    distance_km = float(input())

    current_expenses = distance_km * fuel_km

    if day % 3 == 0 or day % 5 == 0:
        current_expenses *= 1.4

    if day % 7 == 0:
        money_received = current_expenses / people
        current_expenses -= money_received

    expenses += current_expenses

    if expenses > budget:
        flag = False
        break

expenses += food_group + hotel_group

if not flag:
    print(
        f"Not enough money to continue the trip. "
        f"You need {expenses - budget:.2f}$ more."
    )
else:
    print(
        f"You have reached the destination. "
        f"You have {budget - expenses:.2f}$ budget left."
    )
