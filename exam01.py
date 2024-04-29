# 1. 화면에 Hello World 문자열 출력
print('Hello World')
# 2. Mary's cosmetics 출력
print("Mary\'s cosmetics")
# 3. 길동이 소리질렀다. "도둑이야"
print("길동이 소리질렀다. \"도둑이야\"")
# 4. C:\windows를 출력하세요
print("C:\\windows")
# 5. print() 함수와 sep를 이용하여
#   'naver;kakao;sk;samsung 를 출력하세요.
print('naver','kakao','sk','samsung',sep=";")
# 6. s='hello'
#    t='python'
#    출력결과 'hello! python'
print('hello'+'!','python')
# 7. a='123' 의 타입을 출력하세요
a='123'
print(type(a))
# 8. letters = 'python' 문자열의 첫번째와 세번째 문자를 출력하세요
letters = 'python'
print(letters[0],letters[2])
# 9. license_plate = '24가 2210' 일때 뒤에서 4자리만 출력 '2210'
license_plate = '24가 2210'
print(license_plate[-4:])
# 10. "홀짝홀짝홀짝" => "홀홀홀"로 출력
string = "홀짝홀짝홀짝"
print(string[::2])
# 11. string='PYTHON' 을 거꾸로 출력 => "NOHTYP"
string='PYTHON'
print(string[::-1])

# 12.
phone_number="010-1111-2222"
#     출력결과 010 1111 2222
phone_number=phone_number.replace("-"," ")
# 13. a="3", b="4"  print(a+b) 결과
# 14. 화면에 '-'를 80개 출력하세요
print('-'*80)
# 15.
t1='python'
t2='java'
#    출력결과 python java python java python java python java
t3=t1+ ' ' + t2 + ' '
print(t3*4)

# 16  % formatting문자을 사용하여 .
name1 ="김민수"
age1=10
name2 = "이철희"
age2 = 13
# 출력 결과
#   이름: 김민수 나이: 10
#   이름: 이철희 나이: 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))
# 17. 16번을 format() 메소드를 사용하여 출력
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))
# 18. 16번을 f-문자열을 사용하여 출력
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
# 19.  상장주식수 = "5,969,782,550"
#   컴마제거한 수로 출력 "5969782550"
상장주식수 = "5,969,782,550"
print(상장주식수.replace(",",""))

# 20.
분기 = "2020/03(E) (IFRS연결)"
#     => '2020/03'만 출력
print(분기[:7])
# 21.
ticker = 'btc_krw'
#    => 'BTC_KRW'
print(ticker.upper())
# 22. 'hello' =" 'Hello'로 출력
a='hello'
print(a.capitalize())
# 23.
file_name = '보고서.xlsx'
#      이 파일명이 'xlsx' 로 끝나는지 확인
print(file_name.endswith('xlsx'))
# 24.
file_name = '2020_보고서.xlsx'
#       이 파일명이 '2020'으로 시작되는지 확인
print(file_name.startswith('2020'))
# 25.
a='hello world'
#     이 문장을 두개의 문자열 리스트로 출력하세요
print(a.split())
# 26.
ticker = 'btc_krw'
#     이 문자을 'btc' 와 'krw'로 분리하세요
print(ticker.split('_'))
# 27.
date = '2020-05-01'
#    을 년 월 일로 분리하여 출력하세요
print(date.split('-'))