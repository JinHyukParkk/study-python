from pykrx import stock
import yfinance as yf
import numpy as np
from datetime import datetime, timedelta

# 특정 날짜가 주어진 주의 마지막 영업일을 계산
def get_last_business_day_of_week(date):
    friday = date + timedelta((4 - date.weekday()) % 7)
    if friday > date:
        friday -= timedelta(days=7)
    return friday

# KOSPI 200 구성 종목 가져오기
def get_kospi200_tickers(date):
    date_str = date.strftime("%Y%m%d")
    tickers = stock.get_index_portfolio_deposit_file("1028", date=date_str)  # KOSPI 200 인덱스 코드
    return tickers

# KOSPI 200 종목 코드와 이름 매핑
def get_kospi200_stocks(date):
    tickers = get_kospi200_tickers(date)
    kospi200_stocks = []
    for ticker in tickers:
        stock_name = stock.get_market_ticker_name(ticker)
        kospi200_stocks.append((ticker, stock_name))
    return kospi200_stocks

# 오늘 날짜와 1년 전 날짜 계산
now = datetime.now()
one_year_ago = now - timedelta(days=365)
last_business_day = get_last_business_day_of_week(now)

# 현재 날짜를 기준으로 종목 가져오기
kospi200_stocks = get_kospi200_stocks(last_business_day)
print(f"KOSPI 200 종목 수: {len(kospi200_stocks)}")
print(kospi200_stocks)


# 주식 데이터 수집
def get_stock_data(tickers, start_date, end_date):
    data = {}
    for ticker, name in tickers:
        ticker_yahoo = f"{ticker}.KS"  # Yahoo Finance 형식으로 변환
        print(f"Downloading data for {name} ({ticker_yahoo})")
        try:
            stock_data = yf.download(ticker_yahoo, start=start_date, end=end_date)
            if not stock_data.empty:
                data[ticker_yahoo] = stock_data
            else:
                print(f"No data found for {name} ({ticker_yahoo})")
        except Exception as e:
            print(f"Error downloading data for {name} ({ticker_yahoo}): {e}")
    return data


def preprocess_data(stock_data):
    for ticker, data in stock_data.items():
        # 결측값 처리 (앞의 값으로 대체)
        data.fillna(method='ffill', inplace=True)
        data.fillna(method='bfill', inplace=True)
    return stock_data


def extract_features(stock_data):
    features = {}
    for ticker, data in stock_data.items():
        data['50_MA'] = data['Close'].rolling(window=50).mean()
        data['200_MA'] = data['Close'].rolling(window=200).mean()
        data['Volume_Change'] = data['Volume'].pct_change()
        features[ticker] = data
    return features


def recommend_stocks(feature_data):
    recommendations = {}
    for ticker, data in feature_data.items():
        # 단순히 이동 평균 교차를 기준으로 추천
        data['Signal'] = 0
        data['Signal'][data['50_MA'] > data['200_MA']] = 1
        recommendations[ticker] = data['Signal']
    return recommendations


def evaluate_model(recommendations, stock_data):
    results = {}
    for ticker, signals in recommendations.items():
        correct = np.sum((signals == 1) & (stock_data[ticker]['Close'].shift(-1) > stock_data[ticker]['Close']))
        total = np.sum(signals == 1)
        accuracy = correct / total if total > 0 else 0
        results[ticker] = accuracy
    return results


def recommend():
    print("추천 시스템을 시작합니다...")
    today = datetime.now()
    one_year_ago = today - timedelta(days=365)
    start_date = one_year_ago.strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")

    last_business_day = get_last_business_day_of_week(today)
    kospi200_stocks = get_kospi200_stocks(last_business_day)

    if len(kospi200_stocks) == 0:
        print("No KOSPI 200 stocks found.")
        return

    stock_data = get_stock_data(kospi200_stocks, start_date, end_date)

    if len(stock_data) == 0:
        print("No stock data downloaded.")
        return

    processed_data = preprocess_data(stock_data)
    feature_data = extract_features(processed_data)
    recommendations = recommend_stocks(feature_data)
    evaluation_results = evaluate_model(recommendations, processed_data)

    print("추천 결과:")
    for ticker, accuracy in evaluation_results.items():
        print(f"{ticker}: 추천 정확도 {accuracy:.2f}")


recommend()