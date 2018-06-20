import random


def generate_game_data(player_1, player_2):
    return random.choices([player_1.get('name'), player_2.get('name')],
                          [player_1.get('serve'), player_2.get('return')])[0]


def winning_condition_set(score):
    if (score[0] == 6) and (score[1] <= 4):
        return True
    elif (score[1] == 6) and (score[0] <= 4):
        return True
    elif (score[0] == 7) and (score[1] == 6):
        return True
    elif (score[1] == 7) and (score[0] == 6):
        return True
    else:
        return False


def generate_set_data(player_1, player_2):
    score = [0, 0]
    games_won = []
    while not winning_condition_set(score):
        if sum(score) % 2 == 0:
            winning_player = generate_game_data(player_1, player_2)
        else:
            winning_player = generate_game_data(player_2, player_1)
        games_won.append(winning_player)
        if winning_player == player_1.get('name'):
            score[0] += 1
        else:
            score[1] += 1
    return games_won


if __name__ == '__main__':
    romain = {"name": "romain",
              "serve": 50,
              "return": 50}
    king = {"name": "king",
            "serve": 500000,
            "return": 500000}
    result = generate_set_data(king, romain)
    print(result)
