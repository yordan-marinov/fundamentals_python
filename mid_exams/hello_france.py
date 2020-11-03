items = input().split("|")
budget = float(input())

CLOTHES_MAX_PRICE = 50
SHOES_MAX_PRICE = 35
ACCESSORIES_MAX_PRICE = 20.50

TICKET_PRICE = 150


bought_items = []
for item in items:
    token = item.split("->")
    name = token[0]
    price = float(token[1])

    if (
            name == "Clothes" and
            price <= CLOTHES_MAX_PRICE and
            budget >= price
    ):
        bought_items.append(price)
        budget -= price

    elif (
            name == "Shoes" and
            price <= SHOES_MAX_PRICE and
            budget >= price
    ):
        bought_items.append(price)
        budget -= price

    elif (
            name == "Accessories" and
            price <= ACCESSORIES_MAX_PRICE and
            budget >= price
    ):
        bought_items.append(price)
        budget -= price

new_prices = [p * 1.4 for p in bought_items]
profit = sum(new_prices) - sum(bought_items)
total = sum(new_prices) + budget

print(" ".join([f"{n:.2f}" for n in new_prices]))
print(f"Profit: {profit:.2f}")

if total >= TICKET_PRICE:
    print("Hello, France!")
else:
    print("Time to go.")
