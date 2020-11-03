age = int(input())

KIDS = 14
TEENS = 18
YOUNG_ADULTS = 21
ADULTS = 22

if age <= KIDS:
    drink = "toddy"
elif KIDS < age <= TEENS:
    drink = "coke"
elif TEENS < age <= YOUNG_ADULTS:
    drink = "beer"
else:
    drink = "whisky"


print(f'drink {drink}')
