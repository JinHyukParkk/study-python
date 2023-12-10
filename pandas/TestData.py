import pandas as pd


class TestData:
    @staticmethod
    def getData():
        return pd.read_csv('../data/gapminder.tsv', sep='\t')
