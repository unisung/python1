import requests
from bs4 import BeautifulSoup

codes = ['096530', '010130'] # 종목코드 리스트
prices = [] # 가격정보가 담길 리스트
for code in codes:
    url = 'https://finance.naver.com/item/main.nhn?code=' + code
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    today = soup.select_one('#chart_area > div.rate_info > div')
    price = today.select_one('.blind')
    prices.append(price.get_text())

print(prices)