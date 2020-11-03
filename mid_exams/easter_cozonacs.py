budget = float(input())
price_flour = float(input())

pack_eggs = price_flour * 0.75
milk = (price_flour * 1.25) / 4
cake_price = price_flour + pack_eggs + milk

color_eggs = 0
cakes = 0
while budget >= cake_price:
    budget -= cake_price
    cakes += 1
    color_eggs += 3

    if cakes % 3 == 0:
        color_eggs -= (cakes - 2)

print(
    f"You made {cakes} cozonacs! "
    f"Now you have {color_eggs} eggs and {budget:.2f}BGN left."
)
