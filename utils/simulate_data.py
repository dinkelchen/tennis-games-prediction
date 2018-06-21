import random


def set_winner(score):
    if (score[0] == 6) and (score[1] <= 4):
        return 0
    elif (score[1] == 6) and (score[0] <= 4):
        return 1
    elif (score[0] == 7) and (score[1] == 6):
        return 0
    elif (score[1] == 7) and (score[0] == 6):
        return 1
    else:
        return -1


def generate_readable_score_per_set(games_won):
    return [games_won.count(0), games_won.count(1)]


def generate_set_data(player_0, player_1):
    score = [0, 0]
    games_won = []
    services = []
    while set_winner(score) == -1:
        if sum(score) % 2 == 0:
            services.append(0)
            games_won.append(random.choices([0, 1],
                                            [player_0.get('serve'), player_1.get('return')])[0])
        else:
            services.append(1)
            games_won.append(random.choices([1, 0],
                                            [player_1.get('serve'), player_0.get('return')])[0])
        score = generate_readable_score_per_set(games_won)
    return services, games_won


if __name__ == '__main__':
    romain = {"name": "romain",
              "serve": 50,
              "return": 50}
    king = {"name": "king",
            "serve": 50,
            "return": 50}
    _, result = generate_set_data(romain, king)
    print(result)
    print(generate_readable_score_per_set(result))
