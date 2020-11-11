orders = {}

while True:

    data = input()
    if data == "buy":
        [
            print(f"{key} -> {value.pop(0) * sum(value):.2f}")
            for key, value in orders.items()
        ]
        break

    data = data.split()
    product, price, quantity = (
        data[0], float(data[1]), int(data[2])
    )

    if product not in orders:
        orders[product] = []
        orders[product].append(price)
        orders[product].append(quantity)
    else:
        if orders[product][0] != price:
            orders[product][0] = price
        orders[product].append(quantity)
