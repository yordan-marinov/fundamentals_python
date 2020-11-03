budget = float(input())
price_flour_kg = float(input())

eggs_price_pack = price_flour_kg * 0.75
milk_price_liter = price_flour_kg * 1.25
milk_needed_price = milk_price_liter * 0.25

cake_price = (
        eggs_price_pack +
        price_flour_kg +
        milk_needed_price
)

colored_eggs = 0
cakes = 0
while budget > cake_price:
    cakes += 1
    budget -= cake_price
    colored_eggs += 3
    if cakes % 3 == 0:
        colored_eggs -= cakes - 2

print(f"You made {cakes} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
