# 예시 블로그
# https://gojstudio.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%84%A4%EC%9D%B4%EB%B2%84-%EC%A3%BC%EC%8B%9D-%ED%81%AC%EB%A1%A4%EB%A7%81-%EC%98%88%EC%A0%9C-1%ED%8E%B8/

# 1단계: 네이버 주식 종목코드 크롤링
import requests
from bs4 import BeautifulSoup as bs
import openpyxl

# 종목, 종목코드, 현재가 리스트를 담을 빈 리스트
stock_data = []

# 각각 종목, 종목코드를 담을 빈 리스트
stock_names = []
stock_codes = []

# 무한 반복문, 특정 조건을 입력하면 멈춘다.
while True:
    keyword = input("종목 코드를 입력하세요. quit을 입력하면 종목 선택이 끝납니다.")

    if keyword == 'quit':
      break

    stock_names.append(keyword)

    # requests.get 메서드의 params 옵션
    payload_code = {'where' : 'nexearch', 'query' : keyword, 'oquery' : f'{keyword}종목코드'}

    # 쿼리 스트링을 뺀 URL 엔드포인트
    url_code = "https://search.naver.com/search.naver"

    response_code = requests.get(url_code, params=payload_code)
    print(response_code.status_code)
    html_code = response_code.text
    soup_code = bs(html_code, 'html.parser')

   # 네이버 검색 결과에서 증권정보를 보여주는 섹션 태그 클래스
    code_section_tag = 'section.sc_new.cs_stock.cs_stock_same._cs_stock'
    code_section = soup_code.select_one(code_section_tag)
    print(code_section)

    # 검색 결과에 증권정보 섹션이 있을 경우에만 크롤링 데이터를 추출한다.
    if code_section:
      # 종목코드 데이터 추출
      code_data = soup_code.select_one(f'{code_section_tag} .t_nm').text
      # print(code_data)
      # code_data 문자열에서 종목코드만 추출해서 리스트에 추가
      stock_codes.append(code_data[:6])
    else:
      print('없는 종목입니다. 종목 이름을 다시 입력해 주세요.')
      stock_names.remove(keyword)

stock_data.append(stock_names)
stock_data.append(stock_codes)
print(stock_data)