from collections import defaultdict


def get_data():
    players = defaultdict(lambda: defaultdict(int))

    while True:

        data = input()
        if data == "Season end":
            print_statement(players)
            break

        if not " vs " in data:
            data = data.split(" -> ")
            name = data[0]
            position = data[1]
            skill = int(data[2])

            if players[name][position] < skill:
                players[name][position] = skill

            elif players[name][position] >= skill:
                continue
            else:
                players[name][position] += skill
        else:
            data = data.split(" vs ")
            player_1 = data[0]
            player_2 = data[1]

            if player_1 in players and player_2 in players:
                players = battle_players(player_1, player_2, players)


def battle_players(player_1, player_2, dd: dict) -> dict:
    for name_position in dd[player_1].keys():

        if name_position in dd[player_2].keys():
            player_1_total_points = sum(dd[player_1].values())
            player_2_total_points = sum(dd[player_2].values())

            if player_1_total_points > player_2_total_points:
                del dd[player_2]
            elif player_2_total_points > player_1_total_points:
                del dd[player_1]

    return dd


def print_statement(dd: dict) -> print:
    for player, values in sorted(
            dd.items(),
            key=lambda pair: (-sum(pair[1].values()), pair[0])
    ):
        print(f"{player}: {sum(values.values())} skill")

        for positions, value in sorted(
                values.items(),
                key=lambda x: (-x[1], x[0])
        ):
            print(f"- {positions} <::> {value}")


get_data()
