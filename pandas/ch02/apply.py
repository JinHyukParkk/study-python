import pandas as pd

# apply 와 map 의 차이점은
# apply 는 데이터프레임의 행과 열을 반복해서 특정 함수에 적용하고,
# map 은 시리즈의 모든 원소에 특정 함수를 적용한다는 것이다.

init_df_case1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(init_df_case1)

df = init_df_case1.apply(lambda x: x ** 2)
print(df)

df = init_df_case1.map(lambda x: x ** 2)
print(df)


init_df_case2 = pd.DataFrame({'Num': [1, 2, 3], 'Eng': ['A', 'B', 'C']})
print(init_df_case2)

df = init_df_case2.apply(lambda x: x.Num ** 2, axis=1)
print(df)

df = init_df_case2.map(lambda x: x.Num ** 2)
print(df)