import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import yfinance as yf

# 데이터 불러오기 (예: 삼성전자)
ticker = "005930.KS"  # 삼성전자의 Yahoo Finance 티커
start_date = "2020-01-01"
end_date = "2024-06-01"

df = yf.download(ticker, start=start_date, end=end_date)

# 필요한 열만 선택
df = df[['Close']]

# 데이터 정규화
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df)

# 데이터셋 생성
train_data_len = int(np.ceil(len(scaled_data) * 0.8))

train_data = scaled_data[0:train_data_len, :]
test_data = scaled_data[train_data_len - 60:, :]

# 훈련 데이터셋 생성
def create_dataset(data, look_back=60):
    x, y = [], []
    for i in range(len(data) - look_back):
        x.append(data[i:i + look_back, 0])
        y.append(data[i + look_back, 0])
    return np.array(x), np.array(y)

x_train, y_train = create_dataset(train_data)
x_test, y_test = create_dataset(test_data)

# 데이터 reshape: LSTM 모델 입력 형식에 맞게 변환 (samples, time steps, features)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# LSTM 모델 구축
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(units=50, return_sequences=False))
model.add(Dense(units=25))
model.add(Dense(units=1))

# 모델 컴파일
model.compile(optimizer='adam', loss='mean_squared_error')

# 모델 학습
model.fit(x_train, y_train, batch_size=1, epochs=10)

# 예측 데이터셋 생성
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

# 실제 데이터셋 생성
train = df[:train_data_len]
valid = df[train_data_len:]
valid['Predictions'] = predictions

# 시각화
plt.figure(figsize=(16, 8))
plt.title('LSTM Model')
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
plt.show()

# 미래 데이터 예측을 위한 준비
future_days = 30  # 예측하고자 하는 일 수

# 마지막 60일의 데이터를 사용하여 예측 시작
last_60_days = df[-60:].values
scaled_last_60_days = scaler.transform(last_60_days)

# 예측을 위한 빈 리스트 생성
X_test = [scaled_last_60_days]
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# 미래 예측
future_predictions = []
for _ in range(future_days):
    pred = model.predict(X_test)
    future_predictions.append(pred[0, 0])
    # 새로운 데이터 포인트를 추가하여 다음 예측을 위해 사용
    pred_reshaped = np.reshape(pred, (1, 1, 1))
    X_test = np.concatenate((X_test[:, 1:, :], pred_reshaped), axis=1)

# 예측 결과 역정규화
future_predictions = np.array(future_predictions).reshape(-1, 1)
future_predictions = scaler.inverse_transform(future_predictions)

# 예측 결과 시각화
last_date = df.index[-1]
prediction_dates = pd.date_range(last_date, periods=future_days + 1, inclusive='right')

plt.figure(figsize=(16, 8))
plt.title('Stock Price Prediction')
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')
plt.plot(df['Close'])
plt.plot(prediction_dates, future_predictions, color='red', label='Future Predictions')
plt.legend(['Actual', 'Future Predictions'], loc='upper left')
plt.show()
