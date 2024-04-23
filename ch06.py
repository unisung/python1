#제어문
#조건문
# if 조건식:
#     실행문
# 점수를 입력받아서 80점 이상이면 "pass" 출력
#score = int(input("점수:"))
#if score >=80:
#    print("pass")

# 점수를 입력받아서 80점 이상이면 "pass" 출력
# 80점 미만이면 "fail" 출력
'''
score = int(input("점수:"))
if score >=80:
    print("pass")
if score <80:
    print("fail")
'''

# if ~ else:
'''
score = int(input("점수:"))
if score >=80:
    print("pass")
else:
    print("fail")
'''

# if ~elif ~else
'''
score = int(input("점수:"))
if score >=80:
    print("A")
elif score >=70: # 70~79
    print("B")
else: # 0~69
    print("C")
'''
# 90점이상 80점이상 70점이상 60점이상 60점미만
#  A       B       C        D        F
'''
score = int(input("점수:"))
if score >=90:
    print("A")
elif score >=80: # 80~89
    print("B")
elif score >=70: # 70~79
    print("C")
elif score >=60: # 60~69
    print("D")
else: # 0~69
    print("F")
'''
'''
kg = int(input('체중(kg)을 먼저 입력한 후 키(m) 입력 체중:'))
m=float(input('키:'))
bmi = kg / (m**2)
msg = "결과:"
if bmi  >= 40:
    msg+="고도비만"
elif bmi  >= 30: # 30~39
    msg+="비만"
elif bmi  >= 25: # 25~29
    msg+="과체중"
elif bmi  >= 20: # 20~24
    msg+="정상"
else: # 0~19
    msg+="저체중"

print("bmi지수:", f"{bmi:.3f}",msg)
'''
#2. 로그인 처리
'''
id = input('아이디:')
pwd = input('비밀번호:')
if id=='admin' and pwd=='test' :
    print(f'{id}님 hello!')
else:
    print('fail')
'''
'''
#3. 로그인 개선
id =input("ID:")
pw =input("PW:")
if id=="admin": #id가admin이라면
    if pw=="test":#pw가test라면
        print("Hello")
    else: #id는일치하지만비밀번호가틀린경우
        print("WrongPW")
else: #id가admin이아닌경우
    print("WrongID")
'''
'''
# if True인 경우 아무것도 하지 않는 문장
card = True
if card:
    pass
else:
    print('걸어감')
'''
'''
card = True
if card: pass
else: print('걸어감')
'''
'''
#조건부 표현식
score=int(input('점수:'))
# 변수 = 조건문이 참인결과 if 조건문 else 조건문이 거짓인결과
message = "success" if score >=60 else "failure"
print(message)
'''
#'23 12 45'
temp = input().split()
#temp ='23 12 45'.split()
print(temp)

a,b,c = map(int,temp) # ['23','12','45']=>[int('23'),int('12'),int('45')]=> [23,12,45]
print(a,type(a),b, type(b),c,type(c))

for x in temp:
    print(int(x))
