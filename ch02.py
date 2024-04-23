#표준 입출력
#score = input() #외부로부터 입력받는함수
#print(score)
#score = input("점수:")#input 결과는 문자열
#print(type(score))
#print(score)
#score = input("점수:")
#print(int(score)+10)
'''
여러줄 주석
print('I can\'t swim') # escape문자
print("\"파이썬\" 언어")
print("c:\\temp\\myfile.py") #window
print("c:\\temp\\myfile.py") #linux
'''

#연결 연산
#print("Hello" + "Python") # concat
#print("Hello","Python","123") # ,
#print("Hello""Python"" 123") #

#print("Hello",3)
#print("Hello"3)
#print("Hello"+3) # str + int
#print("Hello"*3) # * 반복 연산

#formatting문자열
name ="홍길동"
age = 17
score = 91.35
print("이름:%s"%name)
print("나이:%f"%age)
print("score:%f"%score)
print("이름:%s, 나이:%d, 점수:%f"%(name,age,score))

#% 포매팅
print("[%10s]"%name) #오른쪽 정렬  default
print("[%-10s]"%name)#왼쪽 정렬

score=91.35
print("[%.1f]"%score) # .1f 소수점 1자리
print("[%.3f]"%score) # .3f 소수점 3자리
print("[%8.1f]"%score) # 8.1f 전체 8자리 소수점 1자리,오른쪽정렬default
print("[%8.3f]"%score)# 8.3f 전체 8자리 소수점 3자리,오른쪽정렬default
print("[%-8.1f]"%score)# 8.1f 전체 8자리 소수점 1자리,왼쪽정렬
print("[%-8.3f]"%score)# 8.3f 전체 8자리 소수점 3자리,왼쪽정렬
