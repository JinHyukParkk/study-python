import pandas as pd

s = pd.Series(['banana', 42])
print(s)

print("--------------------")
s = pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Who'])
print(s)

print("--------------------")
scientists = pd.DataFrame({
    "Name": ["hyuk", "suk"],
    "Occupation": ["Chemist", "Statistician"],
    "Born": ["1920-07-25", "1876-06-13"],
    "Died": ["1958-04-16", "1937-10-16"],
    "Age": [31, 30]
})
print(scientists)

print("--------------------")
scientists = pd.DataFrame(
    data={
        "Occupation": ["Chemist", "Statistician"],
        "Born": ["1920-07-25", "1876-06-13"],
        "Died": ["1958-04-16", "1937-10-16"],
        "Age": [31, 30]
    },
    index=["Rosaline Franklin", "William Gosset"],
    columns=["Occupation", "Born", "Age", "Died"]
)
print(scientists)

print("--------------------")
first_row = scientists.loc["William Gosset"]
print(first_row)
print(first_row.keys())
print(first_row.index)

print("--------------------")
ages = scientists["Age"]
print(ages)
print(ages.mean()) # 평균
print(ages.min()) # 최소
print(ages.max()) # 최대
print(ages.std()) # 표준편차는 데이터가 평균에서 얼마나 떨어져 있는지 나타내는 지표이다.
# 표준편차 구하는 방법은 다음과 같다.
# 1. 각 데이터와 평균의 차이를 구한다.
# 2. 1에서 구한 차이를 제곱한다.
# 3. 2에서 구한 제곱의 평균을 구한다.
# 4. 3에서 구한 값의 제곱근을 구한다.

print("--------------------")