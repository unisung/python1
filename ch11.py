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




