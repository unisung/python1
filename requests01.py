import requests

response = requests.get('https://www.naver.com/')

print(response.status_code)
print(response.text)
