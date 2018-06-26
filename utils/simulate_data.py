import random
import pandas as pd


def set_winner(score):
    if (score[0] == 6) and (score[1] <= 4):
        return 0
    elif (score[1] == 6) and (score[0] <= 4):
        return 1
    elif score[0] == 7:
        return 0
    elif score[1] == 7:
        return 1
    else:
        return -1


def generate_readable_score_per_set(games_won):
    return [games_won.count(0), games_won.count(1)]


def generate_set_data(player_0, player_1, serve_first=0):
    score = [0, 0]
    games_won = []
    services = []
    while set_winner(score) == -1:
        if (sum(score) + serve_first) % 2 == 0:
            services.append(0)
            games_won.append(random.choices([0, 1],
                                            [player_0.get('serve'), player_1.get('return')])[0])
        else:
            services.append(1)
            games_won.append(random.choices([1, 0],
                                            [player_1.get('serve'), player_0.get('return')])[0])
        score = generate_readable_score_per_set(games_won)
    return services, games_won


def generate_match_data(player_0, player_1, wins_needed=2):
    sets_won = []
    match = {'services': [], 'games_won': []}
    services, games_won = generate_set_data(player_0, player_1)
    match['services'].append(services)
    match['games_won'].append(games_won)
    sets_won.append(games_won[-1])
    while (sets_won.count(0) < wins_needed) & (sets_won.count(1) < wins_needed):
        services, games_won = generate_set_data(player_0, player_1, 1 - services[-1])
        match['services'].append(services)
        match['games_won'].append(games_won)
        sets_won.append(games_won[-1])

    return match


flatten = lambda l: [item for sublist in l for item in sublist]


def into_pandas_format(match_id, player_0, player_1, match_result):
    server = flatten(match_result.get('services'))
    winner = flatten(match_result.get('games_won'))
    length_of_match = len(server)
    player_names = (player_0.get('name'), player_1.get('name'))
    df = pd.DataFrame(data={'Match_id': [match_id] * length_of_match,
                            'Server': [player_names[i] for i in server],
                            'Returner': [player_names[1 - i] for i in server],
                            'Game_id': range(length_of_match),
                            'Broken': abs(pd.np.array(winner) - pd.np.array(server))})
    return df


if __name__ == '__main__':
    romain = {"name": "romain",
              "serve": 50,
              "return": 50}
    king = {"name": "king",
            "serve": 50,
            "return": 50}
    matches_to_play = 5
    df = pd.DataFrame()
    for i in range(matches_to_play):
        result = generate_match_data(romain, king)
        df = df.append(into_pandas_format(i, romain, king, result), ignore_index=True)

    print(df)
