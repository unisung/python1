#연산자
#산술, 대입, 비교, 논리, 비트
#산술
print(2+3) #더하기
print(4/2) #나누기 실수
print(7%3) #나머지
print(7//3) # 몫
print(2**3) # 제곱 2^3
a=7
b=3
result=f"{a}를 {b}로 나눈 몫은 {a//b}이고, 나머지는{a%b}입니다."
print(result)
#root표현
print(4**0.5)

# 대입 연산자  =
a=5
a=a+1
print(a) #6
a+=2  # a=a+2 # 8
print(a)

a-=4 # a=a-4
print(a)

a+=1
print(a)

#a++
#print(a)

# 비교 연산자
a=5
b=10
print(a>b) # a가 b보다 큰가?
print(a>=b) #a가 b보다 크거나 같은가?
print(a<b) #a가 b보다 작은가?
print(a<=b) #a가 b보다 작거나 같은가?
print(a==b) # a와 b가 같은가?
print(a!=b) # a와 b가 같지 않은가?
print('--------------------------------')
#논리 연산자
# and, or, not
print(True and True)
print( a> 2 and b> 2)
print('--------------')
print( 0 and 1) # 0 -False, 1 -True
print(True and False)
print(True or True)
print( 0 or 1) # 0- False, 1 - True
print(True or False)
print(not True)
print(not False)

# 비트 연산
a=13 # 1101
b=10 # 1010
#      1000
print(a & b)
print( a | b) # 1111
print( a ^ b) # 0111




