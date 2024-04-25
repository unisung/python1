#딕셔너리
#{key1:value1, key2:value2, key3:value1,...}
#key는 중복불가, value는 중복가능
d1={} #빈 딕셔너리
d2={"name":"홍길동",
    "email":"test1@abc.com",
    "phone":"010-1234-5678"}
d3=dict(name="김철수",
        email="test2@abc.com",
        phone="010-8765-4321")
print(type(d1),type(d2),type(d3))

#딕셔너리 item추가
fruits={"a":"apple","b":"banana"}
fruits["c"]="carrot"
print(fruits)

#딕셔너리에 키가중복인 item추가-최종으로 입력된 value로 대체
fruits={"a":"apple","b":"banana"}
fruits["b"]="blueberry"
print(fruits)

#item의 value가 list도 가능
fruits={"a":"apple","b":"banana"}
fruits["c"]=["coconut","cherry"]
print(fruits)

# item삭제는 del 딕셔너리[키]
fruits={"a":"apple","b":"banana"}
del fruits["b"]
print(fruits)

#모든 items삭제 clear
fruits={"a":"apple","b":"banana"}
fruits["c"]=["coconut","cherry"]
print(fruits)
fruits.clear() #모든 요소들 삭제
print(fruits)
# 딕셔너리 내에 존재하지 않는 키 삭제시 오류
#del fruits["k"]

#딕셔너리 내 요소검색
fruits={"a":"apple","b":"banana"}
fruits["c"]=["coconut","cherry"]
print(fruits)

# key in 딕셔너리 True, value in 딕셔너리 False
print("b" in fruits, "banana" in fruits)

# value검색 - values(), keys()
fruits={"a":"apple","b":"banana", "c":"cherry"}
print(fruits.keys(), type(fruits.keys())) # 키 객체
print(fruits.values(),type(fruits.values())) # value 객체
print(fruits.items(),type(fruits.items())) # item객체

for k, v in fruits.items():
    if v=="banana":
        print(k,":",v)

#value존재확인
print("banana" in fruits.values())

# 딕셔너리 합치기 update()
# 합칠때 키가 중복이면 마지막 value로 업데이트됨.
f1={'a':'apple', 'b':'banana'}
f2={'b':'blueberry','c':'coconut'}
f1.update(f2)
print(f1)

# 퀴즈- 리스트를 아래와 같이 dict_bleed{}로 변환하는 코드작성
blist =['A','O','B','AB','B','A','AB','AB','A','A']
dict_bleed={}
# {'A':4, 'B':2, 'AB':3,'O':1}
for x in blist:
    dict_bleed[x] = blist.count(x)
print(dict_bleed)



data={"d":8,"c":5,"a":9,"b":2}
d1=sorted(data)
d2=sorted(data.keys())# []
print(d1,d2)
#딕셔너리 출력
data={"d":8,"c":5,"a":9,"b":2}
d3=sorted(data.keys(),reverse=True)#[]
for k in d3:
    print(k,data[k])

data={"d":8,"c":5,"a":9,"b":2}
d2=sorted(data.values())
d3=sorted(data.values(),reverse=True)
print(d2,d3)

# items() 정렬
data={"d":8,"c":5,"a":9,"b":2}
d1=sorted(data.items())
d2=sorted(data.items(),reverse=True)
print(d1,d2)

#
data={'d':8, 'c':5, 'a':9, 'b':2}
k1=sorted(data.items(),key=lambda x:x[0])
k2=sorted(data.items(),
        key=lambda x:x[0],reverse=True)
print(k1,k2)

v1=sorted(data.items(),key=lambda x:x[1])
v2=sorted(data.items(),
        key=lambda x:x[1],reverse=True)
print(v1,v2)


#최대 최소
data={'d':8, 'c':5, 'a':9, 'b':2}
sdata=sorted(data.items(), key=lambda x:x[1],reverse=True)
for k, v in sdata:
    print(k,v)

# lamba 예약어
# 함수_이름 = lambda 매개변수, 매개변수2,...: 표현식부분
# def 함수_이름(매개변수1,매개변수2,..):
#    return 값
def add(a,b):
    return a+b

result = add(4,3)
print(result)

add = lambda a,b:a+b
result = add(3,4)
print(result)