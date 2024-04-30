# #
# # import itertools
# #
# # print(all([1,2,3])) # 파이썬에서 숫자 0은 False
# # print(all([1,0,3])) #
# # print(any([1,0,3])) #
# #
# # #enumerate
# # for i, name in enumerate(['body','foo','bar']):
# #     if i==1: continue
# #     print(i, name)
# #
# # # eval
# # a=eval('1+2')
# # print(a)
# #
# # #filter - filter(함수, 반복가능객체)
# # def positive(x):
# #     return x> 0 # True
# #
# # print(list(filter(positive,[1,-3,2,0,-5,6])))
# #
# # #isinstance
# # class Person: pass
# # #해당객체 타입여부 확인 isinstance()
# # a=Person()
# # print(isinstance(a,Person))
# #
# # #map
# # def two_times(x):
# #     return x*2
# # print(list(map(two_times,[1,2,3,4])))
# #
# # # max
# # print(max([1,2,3]))
# # #min
# # print(min('python'))
# #
# # # zip
# # ll = zip([1,2,3],
# #          [4,5,6])
# # print(list(ll))
# #
# # ll = zip([1,2,3],
# #          [4,5,6],
# #          [7,8,9])
# # print(list(ll))
# #
# # #표준라이브러리
# # import time
# # for i in range(10):
# #     print(i)
# #     #time.sleep(1)
# #
# # # 최소공배수, 최대공약수 파이썬 3.5 이상
# # import math
# # print(math.gcd(60,100,80))
# # print(math.lcm(15,25)) #파이썬 3.9이상
# #
# # # itertools
# # students=['한민서','황지민','이양철','이광수','김승민']
# # snacks=['사탕','초컬릿','젤리']
# # result = zip(students, snacks)
# # print(list(result))
# #
# # result = itertools.zip_longest(students, snacks,fillvalue='새우깡')
# # print(list(result))
# #
# # import itertools
# # print(list(itertools.permutations(['1','2','3'],2)))
# #
# # import itertools
# # it=itertools.combinations(range(1,46),6)
# # for num in it:
# #     print(num)
#
# # filter(함수, 반복_가능한_데이터)
# def positive(l):
#     result=[]
#     for i in l:
#         if i>0:
#             result.append(i)
#     return result
# print(positive([1,-3,2,0,-5,6]))
#
# def positive2(x): return x>0 #True/False
# print(list(filter(positive2,[1,-3,2,0,-5,6])))
# print(list(filter(lambda x:x>0 ,[1,-3,2,0,-5,6])))
#
#
# #isinstance
# class Person:
#     pass
# a=Person()
# print(isinstance(a,Person))
# b=3
# print(isinstance(b,Person))
#
# #map(f, iterable객체)
# def two_times(list): return [num*2 for num in list]
#
# result = two_times([1,2,3,4])
# print(result)
#
# def two_times2(x): return x*2
# print(list(map(two_times2,[1,2,3,4])))
# print(list(map(lambda x:x*2,[1,2,3,4])))
#
# #zip
# a=[1,2,3]
# b=[4,5,6]
# z=zip(a,b)
# print('z',list(z))
# z1=list(zip(a,b))
# print('z1',z1)
# c=[7,8,9]
# z2=list(zip(z1,c))
# print('z2',z2)
# print(list(zip(a,b,c)))
#
# # 최대공약수(3.5이후), 최소공배수(3.9)
# import math
# print(math.gcd(60,100,80)) #최대공약수
# print(math.lcm(15,25)) #최소공배수
#
# # itertools.zip_longest
# # zip() 순서쌍이 있는것만 zip으로 묶음
# students=['한민서','황치민','이영철','이광수','김승민']
# snacks=['사탕','초컬릿','젤리']
# print(list(zip(students,snacks)))
# import itertools
# #itertools.zip_longest(리스트1,리스트2,fillvalue=값)
# print(list(itertools.zip_longest(students,snacks,
#                                  fillvalue='새우깡')))
#
# # functools.reduce
# #
# def add(data):
#     result = 0
#     for i in data:
#         result +=i
#     return result
#
# data=[1,2,3,4,5]
# print(add(data))
#
# import functools
# #왼쪽에서 오른쪽으로 하나씩 요소를 가져와서 연산함수
# print(functools.reduce(lambda x,y:x+y, data))
#
# #
# students =[
#     ('jane',22,'A'),
#     ('dave',32,'B'),
#     ('sally',17,'B')
# ]
# from operator import itemgetter
#
# print(sorted(students, key=itemgetter(2)))
#
students = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"name": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 17, "grade": 'B'},
]
students2 = [
    {"name": "jane", "age": 2+2, "grade": 'A'},
    {"name": "dave", "age": 3+2, "grade": 'B'},
    {"name": "sally", "age": 1+7, "grade": 'B'},
]
for a in students:
    a['age']=a['age']//10 + a['age']%10
print(students)

# # print(students2)
# # l1=[]
# # for s in students:
# #     l1.append(zip(students, students2))
# #
# # print(list(l1))
# # for i1,i2 in l1:
# #     print('z',i1,i2)
# #print(students.update(students2))
# print(sorted(students, key=itemgetter('age')))
#
# # 특정 디렉토리내 파일들 리스트 만들기 -glob(경로)
# import glob
# print(glob.glob("c:/temp/a*")) #
#
# #환경 변수 확인
# import os
# print(os.environ)
#
# # 파일 실행 os.popen(명령)
# f=os.popen('dir')
# print(f.read())
#
# #zipfile
# # a.txt, b.txt, c.txt
# import zipfile
#
# with zipfile.ZipFile('C:\\Temp\\mytext.zip','w') as myzip:
#     myzip.write('C:\\Temp\\a.txt')
#     myzip.write('C:\\Temp\\b.txt')
#     myzip.write('C:\\Temp\\c.txt')
#
# with zipfile.ZipFile('C:\\Temp\\mytext.zip') as myzip:
#     myzip.extractall()
#
#
# # threading
# import time
# def long_task():
#     for i in range(5):
#         time.sleep(1)
#         print("working:%s\n" %i)
#
# print('start')
#
# for i in range(5):
#     long_task()
#
# print('End')
#
# import time
# import threading
# def long_task():
#     for i in range(5):
#         time.sleep(1)
#         print("working:%s\n" %i)
#
# print('Start')
# threads=[]
# for i in range(5):
#     t = threading.Thread(target=long_task())
#     threads.append(t)
#
# for t in threads:
#     t.start()
# print("End")

# join()
# import time
# import threading
# def long_task():
#     for i in range(5):
#         time.sleep(1)
#         print("working:%s\n" %i)
#
# print('Start')
# threads=[]
# for i in range(5):
#     t = threading.Thread(target=long_task())
#     threads.append(t)
#
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join()  # thread종료시까지 기다림
# print("End")

#json 파일 읽기
# import json
# with open('myinfo.json',encoding='utf8') as f:
#     data = json.load(f)
#
# print(type(data),data)
#
# # json파일 만들기
# import json
# d={'name': '김길동', 'birth': '0325', 'age': 18}
# json_data=json.dumps(d) #
# print(json_data)
#
# json_data2=json.dumps(d, ensure_ascii=False) #unicode변환방지
# print(json_data2)
# #들여쓰기
# json_data3=json.dumps(d, indent=2,ensure_ascii=False) #unicode변환방지
# print(json_data3)
#
# #
# import urllib.request
#
# #SSL 인증서 검증 비활성화 처리
# import ssl
# context = ssl._create_unverified_context()
# def get_wikidocs(page):
#     resource = 'https://wikidocs.net/{}'.format(page)
#     with urllib.request.urlopen(resource, context=context) as s:
#         with open('wikidocs_%s.html'%page,'wb') as f:
#             f.write(s.read())
#
# get_wikidocs(12)
#
#
# # 브라우저 자동 실행
# import webbrowser
# webbrowser.open_new('http://python.org')