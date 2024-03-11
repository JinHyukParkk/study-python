import pandas as pd


list_double_quotes = ["a", "b", "c", "d", "e"]

list_single_quotes = ['a', 'b', 'c', 'd', 'e']

df = pd.DataFrame({'double_quotes': list_double_quotes, 'single_quotes': list_single_quotes})

df.to_csv('convert_list.csv', index=False)

