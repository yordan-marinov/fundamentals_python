cards = input().split()
number_of_shuffles = int(input())
middle = len(cards) // 2


for _ in range(number_of_shuffles):

    current_shuffle = zip(
        cards[:middle], cards[middle:]
    )

    cards.clear()
    for pair in current_shuffle:
        cards.extend(pair)


print(cards)
