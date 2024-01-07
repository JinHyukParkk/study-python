import pandas as pd

# 데이터 a, b 가 있을 때 a 안에 b 문자들이 여러개 존재한다.
# a를 그룹핑하고 그 안에 b의 중복되는 값 제거

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 3, 1, 2, 3, 1, 2, 3]

df = pd.DataFrame({'a': a, 'b': b})
print(df)

# a 그룹핑하고 b에서의 중복되는 값 제거
df = df.groupby('a')['b'].unique().reset_index()

print(df)
