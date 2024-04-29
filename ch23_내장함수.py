#
import itertools

print(all([1,2,3])) # 파이썬에서 숫자 0은 False
print(all([1,0,3])) #
print(any([1,0,3])) #

#enumerate
for i, name in enumerate(['body','foo','bar']):
    if i==1: continue
    print(i, name)

# eval
a=eval('1+2')
print(a)

#filter - filter(함수, 반복가능객체)
def positive(x):
    return x> 0 # True

print(list(filter(positive,[1,-3,2,0,-5,6])))

#isinstance
class Person: pass
#해당객체 타입여부 확인 isinstance()
a=Person()
print(isinstance(a,Person))

#map
def two_times(x):
    return x*2
print(list(map(two_times,[1,2,3,4])))

# max
print(max([1,2,3]))
#min
print(min('python'))

# zip
ll = zip([1,2,3],
         [4,5,6])
print(list(ll))

ll = zip([1,2,3],
         [4,5,6],
         [7,8,9])
print(list(ll))

#표준라이브러리
import time
for i in range(10):
    print(i)
    #time.sleep(1)

# 최소공배수, 최대공약수 파이썬 3.5 이상
import math
print(math.gcd(60,100,80))
print(math.lcm(15,25)) #파이썬 3.9이상

# itertools
students=['한민서','황지민','이양철','이광수','김승민']
snacks=['사탕','초컬릿','젤리']
result = zip(students, snacks)
print(list(result))

result = itertools.zip_longest(students, snacks,fillvalue='새우깡')
print(list(result))

import itertools
print(list(itertools.permutations(['1','2','3'],2)))

import itertools
it=itertools.combinations(range(1,46),6)
for num in it:
    print(num)
