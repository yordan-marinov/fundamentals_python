def side_checker(string):
    result = []
    winning_symbol = None
    for element in string:
        if element in WINNING_SYMBOLS:
            if not result or element in result:
                result.append(element)
                winning_symbol = element
            else:
                if len(result) >= WINNING_SYMBOLS[winning_symbol]:
                    break
                else:
                    result.clear()
                    winning_symbol = None
                    if element in WINNING_SYMBOLS:
                        result.append(element)
                        winning_symbol = element

    return result, winning_symbol


tickets = input().split(",")

VALID_LENGTH_TICKET = 20
WINNING_SYMBOLS = {
    "@": 6,
    "#": 6,
    "$": 6,
    "^": 6,
}

for ticket in tickets:
    ticket = ticket.strip()

    if len(ticket) != VALID_LENGTH_TICKET:
        print("invalid ticket")
        continue

    middle = len(ticket) // 2

    left_side, l_symbol = side_checker(ticket[:middle])
    right_side, r_symbol = side_checker(ticket[middle:])
    correct_side = min(left_side, right_side)

    if (
            (len(left_side) == len(right_side)) and
            (l_symbol == r_symbol) and
            (len(correct_side) in range(6, 11))
    ):
        if len(left_side) == VALID_LENGTH_TICKET // 2:
            print(f'ticket "{ticket}" - {len(correct_side)}{l_symbol} Jackpot!')

        elif len(correct_side) in range(6, 10):
            print(f'ticket "{ticket}" - {len(correct_side)}{l_symbol}')

    else:
        print(f'ticket "{ticket}" - no match')
