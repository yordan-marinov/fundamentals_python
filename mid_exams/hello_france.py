items = input().split("|")
budget = float(input())

MAXIMUM_CLOTHES = 50.00
MAXIMUM_SHOES = 35.00
MAXIMUM_ACCESSORIES = 20.50

TICKETS_PRICE = 150

bought_items = []
for item in items:

    name, price = item.split("->")
    price = float(price)

    if budget >= price and (
            (name == "Clothes" and price <= MAXIMUM_CLOTHES) or
            (name == "Shoes" and price <= MAXIMUM_SHOES) or
            (name == "Accessories" and price <= MAXIMUM_ACCESSORIES)
    ):
        budget -= price
        bought_items.append(price)

new_prices = [p * 1.40 for p in bought_items]
profit = sum(new_prices) - sum(bought_items)

print(" ".join(f"{p:.2f}" for p in new_prices))
print(f"Profit: {profit:.2f}")

if sum(new_prices) + budget >= TICKETS_PRICE:
    print("Hello, France!")
else:
    print("Time to go.")
