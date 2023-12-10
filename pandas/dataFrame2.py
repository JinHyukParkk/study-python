from TestData import TestData

df = TestData.getData()

# def testLoc():
#     print(df.loc[-1])   # KeyError: -1

def testTail():
    print(df.tail(n=1))

def testLoc():
    # 첫번째, 10번째, 1000번째 행 데이터를 추출한다.
    print(df.loc[[0, 9, 999]])

def testLoc2():
    # loc 속성은 열 지정값으로 열 이름을 사용할 수 있다.
    print(df.loc[:, ['country', 'lifeExp', 'gdpPercap']])

def testIloc():
    # 첫번째, 10번째, 1000번째 행 데이터를 추출한다.
    print(df.iloc[[0, 9, 999]])

def testIloc2():
    # iloc 속성은 열 지정값으로 열 번호를 사용할 수 있다.
    print(df.iloc[:, [0, 3, 5]])

def testRange():
    # range 메서드는 지정된 범위의 정수를 반환한다.
    print(range(5))
    print(range(0, 5))
    print(list(range(5)))
    print(list(range(0, 5)))
    print(list(range(0, 5, 2)))