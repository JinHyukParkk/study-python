import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df)

df = df.apply(lambda x: x ** 2)
print(df)

df = df.apply(lambda x: x ** 2, axis=1)
print(df)

df = df.applymap(lambda x: x ** 2)
print(df)

