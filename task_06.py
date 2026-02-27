class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(args):
    if len(args) != 2:
        raise WrongNumberOfPlayersError()

    player1, player2 = args
    move1 = player1[1]
    move2 = player2[1]
    valid_moves = {'R', 'P', 'S'}

    if player1[1] not in valid_moves or player2[1] not in valid_moves:
        raise NoSuchStrategyError()

    winning_combinations = {
        'R': 'S',
        'S': 'P',
        'P': 'R'
    }

    if player1[1] == player2[1]:
        return f'{player1[0]} {move1}'
    elif winning_combinations[move1] == move2:
        return f"{player1[0]} {move1}"
    else:
        return f"{player2[0]} {move2}"
