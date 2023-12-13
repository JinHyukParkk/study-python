from TestData import TestData

df = TestData.getData()

def testGroup():
    print(type(df.groupby('year')))
    print(type(df.groupby('year')['lifeExp']))
    print(df.groupby('year')['lifeExp'].mean())

def testGroup2():
    # reset_index() 는 인덱스를 새로 부여한다.
    print(df.groupby('year')['lifeExp'].mean().reset_index())