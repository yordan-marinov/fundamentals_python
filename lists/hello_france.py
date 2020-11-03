items = input().split("|")
budget = int(input())

TICKETS_PRICE = 150
INCREASE_BY_PRESENT = 1.4

maximum_prices = {
    "Clothes": 50.00,
    "Shoes": 35.00,
    "Accessories": 20.50,
}

bought_items = []

for item in items:
    item = item.split("->")
    type_item = item[0]
    price_item = float(item[1])

    if (
             price_item <= maximum_prices[type_item] and
            budget >= price_item
    ):
        budget -= price_item
        bought_items.append(price_item)


bought_items_profit = [i * INCREASE_BY_PRESENT for i in bought_items]
profit = sum(bought_items_profit) - sum(bought_items)

print(" ".join([f"{x:.2f}" for x in bought_items_profit]))
print(f"Profit: {profit:.2f}")

if sum(bought_items_profit) + budget >= TICKETS_PRICE:
    print("Hello, France!")
else:
    print("Time to go.")
