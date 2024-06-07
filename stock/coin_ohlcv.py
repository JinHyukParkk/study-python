import ccxt
import pandas as pd
import time

# 데이터 불러오기 (오늘 날짜 기준 7일 전)
from_timestamp = time.time() - 86400 * 7

exchange = ccxt.binance()

# 코인 설정
symbol = 'BTC/USDT'

# OHLCV 데이터 불러오기
ohlcv = exchange.fetch_ohlcv(symbol, '1d', int(from_timestamp * 1000))

# 데이터 프레임 생성
df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

# 등락률 계산
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df['change'] = (df['close'] - df['open']) / df['open']

# 결과 확인
print(df.head())
df.to_csv('BTC_price.csv')


