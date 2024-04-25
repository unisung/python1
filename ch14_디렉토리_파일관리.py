# os, shutil
import os
# print(os.getcwd()) #current디렉토리 출력
# os.chdir(r'c:\temp') #디렉토리 변경
# print(os.getcwd())

#listdir
f1=os.listdir()
#f2=os.listdir('test')
f3=os.listdir(r'C:\temp')
print(f1,f3, sep='\n')
print(os.getcwd())

#scandir() - iterator
file_list = os.scandir()
print(file_list)

for filename in file_list:
    print(filename, filename.name)

#generator로 리턴
t=os.walk(r'C:\Temp')
print(t)
for path, folders, files in t:
    print(path)
    print(folders)
    print(files)

#iterator
a=[1,2,3]
ia=iter(a) # iter() - 이터레이터 생성
print(next(ia))
print(next(ia))
print(next(ia))
print(type(ia))

a=[1,2,3]
ia=iter(a)
for i in ia:
    print(i)

#generator
def mygen():
    yield 'a'
    yield 'b'
    yield 'c'

g=mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))

def mygen2():
    for i in range(1,1000):
        result = i*i
        yield result

gen=mygen2()

print(next(gen))
print(next(gen))
print(next(gen))