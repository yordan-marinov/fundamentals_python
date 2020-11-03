MAX_BAR_LENGTH = 10


def loading_bar(number):
    bar_length = number // MAX_BAR_LENGTH
    if bar_length == MAX_BAR_LENGTH:
        return f"{number}% Complete!\n" \
               f"[{''.join('%' for _ in range(bar_length))}]"
    else:
        bar = ''.join(
                   ['%' for _ in range(bar_length)] +
                   ['.' for _ in range(MAX_BAR_LENGTH - bar_length)]
        )
        return f"{number}% [{bar}]\nStill loading..."


num = int(input())

print(loading_bar(num))
