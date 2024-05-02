# beautifulsoup
# requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
#웹에서 정보 가져오기
html = requests.get('https://search.naver.com/search.naver?query=날씨')
#pprint(html.text)

#파싱
soup=bs(html.text, 'html.parser')

# <div class='detail_box'>
data1 = soup.find('div',{'class':'report_card_wrap'})
pprint(data1)

data2=data1.findAll('li')
pprint(data2)