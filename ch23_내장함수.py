#
# import itertools
#
# print(all([1,2,3])) # 파이썬에서 숫자 0은 False
# print(all([1,0,3])) #
# print(any([1,0,3])) #
#
# #enumerate
# for i, name in enumerate(['body','foo','bar']):
#     if i==1: continue
#     print(i, name)
#
# # eval
# a=eval('1+2')
# print(a)
#
# #filter - filter(함수, 반복가능객체)
# def positive(x):
#     return x> 0 # True
#
# print(list(filter(positive,[1,-3,2,0,-5,6])))
#
# #isinstance
# class Person: pass
# #해당객체 타입여부 확인 isinstance()
# a=Person()
# print(isinstance(a,Person))
#
# #map
# def two_times(x):
#     return x*2
# print(list(map(two_times,[1,2,3,4])))
#
# # max
# print(max([1,2,3]))
# #min
# print(min('python'))
#
# # zip
# ll = zip([1,2,3],
#          [4,5,6])
# print(list(ll))
#
# ll = zip([1,2,3],
#          [4,5,6],
#          [7,8,9])
# print(list(ll))
#
# #표준라이브러리
# import time
# for i in range(10):
#     print(i)
#     #time.sleep(1)
#
# # 최소공배수, 최대공약수 파이썬 3.5 이상
# import math
# print(math.gcd(60,100,80))
# print(math.lcm(15,25)) #파이썬 3.9이상
#
# # itertools
# students=['한민서','황지민','이양철','이광수','김승민']
# snacks=['사탕','초컬릿','젤리']
# result = zip(students, snacks)
# print(list(result))
#
# result = itertools.zip_longest(students, snacks,fillvalue='새우깡')
# print(list(result))
#
# import itertools
# print(list(itertools.permutations(['1','2','3'],2)))
#
# import itertools
# it=itertools.combinations(range(1,46),6)
# for num in it:
#     print(num)

# filter(함수, 반복_가능한_데이터)
def positive(l):
    result=[]
    for i in l:
        if i>0:
            result.append(i)
    return result
print(positive([1,-3,2,0,-5,6]))

def positive2(x): return x>0 #True/False
print(list(filter(positive2,[1,-3,2,0,-5,6])))
print(list(filter(lambda x:x>0 ,[1,-3,2,0,-5,6])))


#isinstance
class Person:
    pass
a=Person()
print(isinstance(a,Person))
b=3
print(isinstance(b,Person))

#map(f, iterable객체)
def two_times(list): return [num*2 for num in list]

result = two_times([1,2,3,4])
print(result)

def two_times2(x): return x*2
print(list(map(two_times2,[1,2,3,4])))
print(list(map(lambda x:x*2,[1,2,3,4])))

#zip
a=[1,2,3]
b=[4,5,6]
z=zip(a,b)
print('z',list(z))
z1=list(zip(a,b))
print('z1',z1)
c=[7,8,9]
z2=list(zip(z1,c))
print('z2',z2)
print(list(zip(a,b,c)))

# 최대공약수(3.5이후), 최소공배수(3.9)
import math
print(math.gcd(60,100,80)) #최대공약수
print(math.lcm(15,25)) #최소공배수

# itertools.zip_longest
# zip() 순서쌍이 있는것만 zip으로 묶음
students=['한민서','황치민','이영철','이광수','김승민']
snacks=['사탕','초컬릿','젤리']
print(list(zip(students,snacks)))
import itertools
#itertools.zip_longest(리스트1,리스트2,fillvalue=값)
print(list(itertools.zip_longest(students,snacks,
                                 fillvalue='새우깡')))

# functools.reduce
#
def add(data):
    result = 0
    for i in data:
        result +=i
    return result

data=[1,2,3,4,5]
print(add(data))

import functools
#왼쪽에서 오른쪽으로 하나씩 요소를 가져와서 연산함수
print(functools.reduce(lambda x,y:x+y, data))

#
students =[
    ('jane',22,'A'),
    ('dave',32,'B'),
    ('sally',17,'B')
]
from operator import itemgetter

print(sorted(students, key=itemgetter(2)))

students = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"name": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 17, "grade": 'B'},
]
print(sorted(students, key=itemgetter('age')))