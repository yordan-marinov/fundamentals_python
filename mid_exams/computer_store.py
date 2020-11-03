TAX = 1.20
# Tax is 20%.
DISCOUNT = 0.9
# Discount is 10%.


def receipt():

    customer_order = 0
    while True:
        type_customer = input()

        if type_customer == "special" or type_customer == "regular":

            if customer_order == 0:
                print("Invalid order!")

            else:
                order_taxed = customer_order * TAX

                print("Congratulations you've just bought a new computer!")
                print(f"Price without taxes: {customer_order:.2f}$")
                print(f"Taxes: {order_taxed - customer_order:.2f}$")
                print("-----------")

                if type_customer == "special":
                    order_taxed *= DISCOUNT

                print(f"Total price: {order_taxed:.2f}$")

            break

        price = float(type_customer)

        if price < 0:
            print("Invalid price!")
            continue

        customer_order += price


receipt()
