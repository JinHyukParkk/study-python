import pandas as pd
from pykrx import stock
from datetime import datetime, timedelta

start_date = '2024-01-01'
end_date = '2024-06-30'

stock_code = input("종목 코드를 입력하세요.")

# 데이터 불러오기
ohlcv = stock.get_market_ohlcv_by_date(start_date, end_date, stock_code)
fundamental_df = stock.get_market_fundamental_by_date(start_date, end_date, stock_code)

# 병합된 데이터 프레임 생성
merge_df = pd.concat([ohlcv, fundamental_df], axis=1)

# 결과 확인
print(merge_df.head())

# 결과를 csv 파일로 저장
merge_df.to_csv(f'{stock_code}_price.csv')