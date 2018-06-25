import pandas as pd

from utils.simulate_data import generate_match_data, into_pandas_format


class SimpleBaseline:
    def __init__(self):
        self.serve_winning_percentage = None

    def fit(self, X, y):
        self.serve_winning_percentage = (X['Server'] == y).mean()

    def predict(self, X):
        return X['Server'].apply(
            lambda x: 1 - self.serve_winning_percentage if x == 0 else self.serve_winning_percentage)


def main():
    romain = {"name": "romain",
              "serve": 50,
              "return": 10}
    king = {"name": "king",
            "serve": 50,
            "return": 10}
    matches_to_play = 5
    df = pd.DataFrame()
    for i in range(matches_to_play):
        result = generate_match_data(romain, king)
        df = df.append(into_pandas_format(i, romain, king, result), ignore_index=True)

    num_records = df.shape[0]
    train_size = int(num_records * 0.8)
    train = df[:train_size]
    test = df[train_size:]

    classifier = SimpleBaseline()
    classifier.fit(train.drop('Winner', axis=1), train['Winner'])
    predictions = classifier.predict(test.drop('Winner', axis=1))
    print(pd.concat([predictions, test['Winner']], axis=1))


if __name__ == '__main__':
    main()
