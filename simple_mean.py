import pandas as pd
from sklearn.metrics import log_loss
from utils.simulate_data import generate_match_data, into_pandas_format


class SimpleMean:
    def __init__(self):
        self.breaking_percentage = None

    def fit(self, X, y):
        self.breaking_percentage = y.mean()

    def predict(self, X):
        return pd.np.repeat(self.breaking_percentage, X.shape[0])


def main():
    romain = {"name": "romain",
              "serve": 50,
              "return": 1}
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

    classifier = SimpleMean()
    classifier.fit(train.drop('Broken', axis=1), train['Broken'])
    predictions = classifier.predict(test.drop('Broken', axis=1))
    print(log_loss(test['Broken'], predictions))


if __name__ == '__main__':
    main()
