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

# f1 = data2[0].find('span',{'class':'txt'})
# f10 = data2[0].find('strong',{'class':'title'})
# print(f10.text,':', f1.text)
# f2 = data2[1].find('span',{'class':'txt'})
# f20 = data2[1].find('strong',{'class':'title'})
# print(f20.text,':', f2.text)
# f3 = data2[2].find('span',{'class':'txt'})
# f30 = data2[2].find('strong',{'class':'title'})
# print(f30.text,':', f3.text)
# f4 = data2[3].find('span',{'class':'txt'})
# f40 = data2[3].find('strong',{'class':'title'})
# print(f40.text,':', f4.text)

for i in data2:
    print(i.find('strong',{'class':'title'}).text,
          i.find('span',{'class':'txt'}).text)

data3 = soup.find('div',{'class':'temperature_text'})
pprint(data3)
pprint(data3.text)

data4 = soup.find('div',{'class':'temperature_info'})
pprint(data4)
pprint(data4.text)

data5 = soup.find('p',{'class':'summary'})
pprint(data5)
pprint(data5.text)
data6 = soup.find('dl',{'class':'summary_list'})
pprint(data6)
pprint(data6.text)

