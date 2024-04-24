# 튜플() 항목 수정불가,삭제불가
#insert, del, remove, pop, sort, reverse 사용불가
print(dir((1,2)))
print(dir([1,2]))
#튜플생성
f2=([5]) #리스트
f22=([5],)
f=(1) # int 1
f1=(1,) # 요소가 하나인 튜플
a=(5,3,1,4,2) #표기법
b=tuple((5,3,1,4,2)) #tuple()함수
b=tuple([5,3,1,4,2])
c=("python",500,3.14)
d=([1,3,2],(10,30,20),"java","C++")
print(type(f2),type(f22),type(f),type(f1),type(a),type(b),type(c), type(d))

#튜플과 리스트 변환
data1=[1,2,3,4,5]
data2=(1,2,3,4,5)
v1 = tuple(data1)
v2 = list(data2)
print(v1,v2)

data2 = list(data2)
print(data2)
data2[2]=6
print(data2)
data2=tuple(data2)
print(data2)

a=("python","C++","JAVA","GO")
b=(4,2,5,1,3)
print(a[1:2]) # 1<= <2
print(a[1:3]) # 1<= <3
print(a[-3:-1]) # -3<= <-1
print(a.index("JAVA"))
print(a.count("C++"))
print(len(a))
c=sorted(b)#원본 데이타는 변함없음, 리턴된 데이타는 정렬된list
print(b)
print(c)

