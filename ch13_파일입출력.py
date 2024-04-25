#파일입출력
'''
f=open('c:/Temp/pro.txt','r')
t=f.readlines() # 여러줄은 한번에 읽어서 list형태출력
print(type(t),t)
f.close()

f=open('c:/Temp/pro.txt','r')
t=f.readline() # 여러줄은 한번에 읽어서 list형태출력 '파이썬'
print(type(t),t)
t=f.readline() #한번에 한줄씩 읽음 '자바'
print(t)
f.close()

f=open('c:/Temp/pro.txt','r')
tt=f.read() #문서전체 내용을 한번에 읽음 '파이썬\n자바'
print(type(tt),tt)
f.close()
'''
#autocloseable with open() as 별칭:
'''
with open('c:/Temp/pro.txt', 'r', encoding='utf8') as f:
    t=f.readline()
    print(t)
'''
# readline()
# with open('c:/Temp/pro.txt', 'r', encoding='utf8') as f:
#     while True:
#         t=f.readline()
#         if not t: break
#         print(t, end='')

#  # readlines()
# with open('c:/Temp/pro.txt', 'r', encoding='utf8') as f:
#     t=f.readlines()
#     for k in t:
#         print(k.replace('\n',''))
#
#
# # 기록하기
# f=open('c:\\Temp\\test.txt','w')
# f.write('python\n')
# f.write('java\n')
# f.close()
# print('저장완료')
#
# # 표준출력 print('값',파일변수)
# f=open('c:\\Temp\\test1.txt','w')
# print('python',file=f)
# print('java',file=f)
# f.close()
# print('저장완료')
#
# # 표준출력 write메소드 혼용
# with open('c:\\Temp\\test2.txt','w') as f:
#     f.write('python\n')
#     print('java',file=f)
#
# ## 파이썬, 자바, 스프링, html, Django 를 한줄씩 파일에 저장 후
# ## 내용을 읽어서 한줄씩 출력
# #파일명 =c:\\myfold\\test4.txt
#
# with open('c:\\Temp\\test4.txt','w') as f:
#     f.write('파이썬\n')
#     f.write('자바\n')
#     f.write('스프링\n')
#     f.write('html\n')
#     f.write('Django\n')
#     print('저장완료')
#
# with open('c:\\Temp\\test4.txt','r') as f:
#     while True:
#         t=f.readline()
#         if not t: break
#         print(t, end='')

#문자열,숫자값 입/출력 -> 객체 입출력
import pickle
f=open("c:\\Temp\\test5.txt",'wb') #w-write,b-binary
blist=['A','B','AB','O','AB','O','B','AB']
data= {}
for x in blist:
    data[x]=blist.count(x)
pickle.dump(data,f)
f.close()
print('저장완료')

f=open("c:\\Temp\\test5.txt",'rb')
data=pickle.load(f)
print(data)
# 퀴즈
# ['A','B','AB','O','AB','O','B','AB']
# {'A':1, 'B':2, 'AB':3, 'O':2}
# c:\temp\blood.txt 저장 후 읽어서 출력






