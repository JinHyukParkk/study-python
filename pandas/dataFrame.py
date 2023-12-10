from TestData import TestData

# pandas 에서는 데이터프레임(DataFrame)과 시리즈(Series) 라는 두 가지 새로운 자료형을 제공한다.
# 데이터프레임은 엑셀에서 볼 수 있는 시트(Sheet)와 동일한 개념이다.
# 시리즈는 엑셀에서 볼 수 있는 열(Column)과 동일한 개념이다.

df = TestData.getData()


def last_row_number(df):
    number_of_rows = df.shape[0]
    last_row_index = number_of_rows - 1
    print(last_row_index)
    return last_row_index

def extract_column(df):
    # 데이터프레임에서 열을 추출하려면 대괄호와 열 이름을 사용하면 된다.
    # Series 자료형이 반환된다.
    country_df = df['country']
    print(country_df.head())
    print(country_df.tail())
    print(type(country_df))

    # 여러 개의 열을 추출하려면 리스트에 열 이름을 담아서 전달하면 된다.
    # DataFrame 자료형이 반환된다.
    subset = df[['country', 'continent', 'year']]
    print(subset.head())
    print(type(subset))

    # loc 속성은 인덱스를 기준으로 행 데이터 추출한다.
    # 인덱스는 데이터프레임의 행 번호를 말한다.
    # Series 자료형이 반환된다.
    print(df.loc[0])
    print(type(df.loc[0]))

    # iloc 속성은 데이터 순서를 의미하는 행 번호를 기준으로 행 데이터 추출한다.
    # iloc 속성은 행 번호를 의미하는 정수(integer)만 받는다.
    # Series 자료형이 반환된다.
    print(df.iloc[0])
    print(type(df.iloc[0]))


extract_column(df)

def data_frame_info(df):
    # shape 는 메서드가 아니라 속성이고, 열과 행의 개수를 튜플로 반환한다.
    print(df.shape)

    # columns 는 데이터프레임의 열 이름을 리스트로 반환한다.
    print(df.columns)

    # dtypes 는 데이터프레임의 열 데이터 타입을 반환한다.
    print(df.dtypes)

    # info 는 데이터프레임의 기본 정보를 출력한다.
    print(df.info())


