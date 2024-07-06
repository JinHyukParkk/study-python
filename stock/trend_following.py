from pykrx import stock
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import talib

# 특정 주식의 데이터를 가져옵니다 (예: 삼성전자)
ticker = "281740"
start_date = "2023-01-01"
end_date = "2024-06-30"

# 일별 주가 데이터를 가져옵니다
df = stock.get_market_ohlcv_by_date(start_date, end_date, ticker)
df = df[['시가', '고가', '저가', '종가', '거래량']]

# 데이터프레임의 인덱스를 DateTime 형식으로 변환
df.index = pd.to_datetime(df.index)

print(df.head())

# 이동 평균 계산
df['50_MA'] = df['종가'].rolling(window=50).mean()  # 50일 이동 평균
df['100_MA'] = df['종가'].rolling(window=100).mean()  # 100일 이동 평균

print(df[['종가', '50_MA', '100_MA']].tail(10))

# 매수/매도 신호 생성
df['Signal'] = 0
df['Signal'][50:] = np.where(df['50_MA'][50:] > df['100_MA'][50:], 1, 0)
df['Position'] = df['Signal'].diff()

print(df[['종가', '50_MA', '100_MA', 'Signal', 'Position']].tail(10))

# ATR 계산
df['ATR'] = talib.ATR(df['고가'], df['저가'], df['종가'], timeperiod=14)
# 현재 종가에서 ATR의 2배를 뺀 값을 손절 라인으로 설정
df['ATR_Stop_Loss'] = df['종가'] - 2 * df['ATR']

# 볼린저 밴드 계산
df['20_MA'] = df['종가'].rolling(window=20).mean()
df['std_dev'] = df['종가'].rolling(window=20).std()
df['Upper_Band'] = df['20_MA'] + 2 * df['std_dev']
df['Lower_Band'] = df['20_MA'] - 2 * df['std_dev']

print(df[['종가', 'ATR', 'ATR_Stop_Loss', 'Upper_Band', 'Lower_Band']].tail(10))

# 역사적 변동성 계산
df['Daily_Return'] = df['종가'].pct_change()
df['Volatility'] = df['Daily_Return'].rolling(window=60).std() * np.sqrt(252)  # 연간화된 변동성

print(df[['종가', 'Volatility']].tail(10))

# 시각화
fig, ax1 = plt.subplots(figsize=(14, 7))

ax1.plot(df['종가'], label='Price', color='black')
ax1.plot(df['50_MA'], label='50-Day MA', color='blue')
ax1.plot(df['100_MA'], label='100-Day MA', color='red')
ax1.plot(df['Upper_Band'], label='Upper Bollinger Band', color='magenta', linestyle='--')
ax1.plot(df['Lower_Band'], label='Lower Bollinger Band', color='cyan', linestyle='--')
ax1.plot(df['ATR_Stop_Loss'], label='ATR Stop-Loss', color='orange', linestyle='--')
ax1.plot(df[df['Position'] == 1].index, df['50_MA'][df['Position'] == 1], '^', markersize=10, color='g', label='Buy Signal')
ax1.plot(df[df['Position'] == -1].index, df['50_MA'][df['Position'] == -1], 'v', markersize=10, color='r', label='Sell Signal')

# 두 번째 y축 추가
ax2 = ax1.twinx()
ax2.plot(df['Volatility'], label='Volatility', color='purple', linestyle='--')
ax2.set_ylabel('Volatility')

# 제목과 범례 설정
ax1.set_title('50-Day and 100-Day Moving Averages with Buy/Sell Signals, ATR Stop-Loss, Bollinger Bands, and Historical Volatility')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()