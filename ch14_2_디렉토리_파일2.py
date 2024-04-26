#
import os
path=r'c:\Temp'

for flist in os.scandir(path):
    if os.path.isfile(flist) and flist.name[-3:]=='txt':# 'test1.txt'
        print(flist.name)

#
fname='test.txt'
file1=fname.split('.')
print(file1, file1[0],file1[1])

for flist in os.scandir(path):
    if os.path.isfile(flist):
        file1=flist.name
        f=file1.split('.')
        if f[1]=='txt':
           #flist.name.split('.')[1]=='txt'):# 'test1.txt'
            print(flist.name)

#
fname='python-3.9.7-amd64.exe'
file1=fname.split('.')
print(file1, file1[:-1], file1[-1]) # [시작:끝], [:]
print(''.join(file1[:-1]),'.',file1[-1])
print(''.join(file1[:-1])+'.'+file1[-1])
id='hong'
pwd='1234'
a='http://www.naver.com'
b='/myapp/login?'
c=f'id={id}&pwd={pwd}'
print(''.join([a,b,c]))# 'http://www.naver.com/myapp/login?id=hong&pwd=1234'
print(''.join([a,b,c]).split('/'))

print('-------------------------------')
# splitext()
for flist in os.scandir(path):
    if os.path.isfile(flist):
        fn, fe = os.path.splitext(flist) #확장자추출 .확장자(.txt)
        print(flist, fn,fe)
        if fe =='.py':
            print(flist.name)

