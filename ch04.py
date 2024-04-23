# format 메소드
name="홍길동"
age=18
score=93.51
print("이름:{}, 나이:{}, 점수:{}".format(name, age, score))
print("이름:{1}, 나이:{2}, 점수:{0}".format(score, name, age))

print("[{:>10}]".format(name))
print("[{:<10}]".format(name))
print("[{:^10}]".format(name))
print("[{:.5f}]".format(score))
print("[{:8.3f}]".format(score))
print("[{:<8.3f}]".format(score))
print("[{:>8.3f}]".format(score))
print("[{:,}]".format(1230000))

#>기호 앞에 문자열을 쓰면 공백을 해당 문자열로 채워줌
print("[{:*>10}]".format(name))
print("[{:#<10}]".format(name))
print("[{:?^10}]".format(name))

#분리후 사용
temp = "이름:{}, 나이:{}, 점수:{}"
temp = temp.format(name,age,score)
print(temp)

# f문자열
# 파이썬 3.6부터 지원
print(f"이름:{name}, 나이:{age}, 점수:{score}")
print(f"[{name:>10}],[{age:>10}]")
print(f"[{name:<10}],[{age:<10}]")
print(f"[{name:^10}],[{age:^10}]")

# 포맷팅을 url 작성하기
site = "https://api.thingspeak.com/update?api_key="
apikey="YTRUYF6Y045MOB37"
v1=5
v2=10
url=f"{site}{apikey}&field1={v1}&field2={v2}"
print(url)
url2 ="%s%s&field1=%d&field2=%d"%(site,apikey,v1,v2)
print(url2)
url3 ="{}{}&field1={}&field2={}".format(site,apikey,v1,v2)
print(url3)