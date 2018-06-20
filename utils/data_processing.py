import pandas


def data_parser(file_name):
    df = pandas.read_csv(file_name, nrows=200)
    return df


def process_pbp(game):
    game = game.replace('A', 'S')
    game = game.replace('D', 'R')
    server_wins = game.count('S')
    returner_wins = game.count('R')
    if server_wins > returner_wins:
        return 'server'
    else:
        return 'returner'


def process_data(raw_df):
    filtered_df = raw_df[['pbp_id', 'server1', 'server2', 'winner', 'pbp']]
    processed_data = []
    for _, row in filtered_df.iterrows():
        games = row['pbp'].split(';')
        for i, game in enumerate(games):
            winner = process_pbp(game)
            if (winner == 'server' and i % 2 == 0) or (winner == 'returner' and i % 2 == 1):
                winner_name = row['server1']
            elif (winner == 'server' and i % 2 == 1) or (winner == 'returner' and i % 2 == 0):
                winner_name = row['server2']
            processed_data.append({'match_id': row['pbp_id'],
                             'player_1': row['server1'],
                             'player_2': row['server2'],
                             'game_id': i,
                             'server': row['server1'] if i % 2 == 0 else row['server2'],
                             'winner': winner_name})
    processed_df = pandas.DataFrame(processed_data)
    return processed_df


if __name__ == '__main__':
    df = data_parser("../data/raw_tennis.csv")
    processed_df = process_data(df)
    print(processed_df)