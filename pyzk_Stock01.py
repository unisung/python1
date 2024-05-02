import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = 'https://finance.naver.com/'
#페이지 정보얻기
response = requests.get(url)
response.raise_for_status()
html = response.text
#페이지 파싱
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.select_one('#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody')
trs = tbody.select('tr')
datas = []
for tr in trs:
    name=tr.select_one('th > a').get_text()
    current_price = tr.select_one('td').get_text()
    change_direction = tr['class'][0]
    change_price = tr.select_one('td > span').get_text()
    datas.append([name, current_price, change_direction, change_price])

write_wb = Workbook()
write_ws = write_wb.create_sheet('결과')
for data in datas:
        write_ws.append(data)

write_wb.save(r'c:/Temp/파일이름.xlsx')
