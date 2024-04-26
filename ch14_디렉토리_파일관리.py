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

## 폴더 생성,삭제, 이름 변경
print(os.getcwd())
result='존재' if os.path.exists('test') else '존재하지 않음'
#os.mkdir('test')
res = 'ok' if False else 'not ok'
print(res)
#특정디렉토리 내에 하위 디렉토리 생성 - 상위경로\경로 지정
#os.mkdir(r'test\tt') # regular expression
#os.mkdir('test\\tt')
#전체 절대경로로 디렉토리 생성
#os.mkdir('c:\\temp\\myfolder')
#os.mkdir(r'c:\temp\myfolder1')
#os.mkdir('c:/temp/myfolder2')

#중간폴더 없는 경우
#os.mkdir('c:/temp/aa/bb')
#os.makedirs('c:/temp/aa/bb')
# os.makedirs('c:\\temp\\aaa\\bbb\\ccc')
#os.makedirs(r'c:\temp\aaaa\bbba\ccca')

#폴더 삭제
#path=r'c:\temp\aaaa\bbba\ccca'
#os.rmdir(path) # 비어있는 폴더 정상 삭제

#비어있지 않는 폴더 삭제시 오류 발생
#path=r'c:\temp\aaaa\bbba'
#os.rmdir(path)

#파일삭제
#os.remove('test.txt')
#os.remove(r'c:\Temp\aaaa\bbba\새 텍스트 문서.txt')

#디렉토리내 파일 삭제 후 디렉토리 정상 삭제됨
#path=r'c:\temp\aaaa\bbba'
#os.rmdir(path)

#os.unlink(r'c:\Temp\aaaa\test.txt')

# os.path.isfile(파일명) -파일 존재여부확인
path = r'c:\Temp\aaaa\mytest.txt'
if os.path.isfile(path):
    os.remove(path)
else:
    print('파일이 없습니다.')

if os.path.exists(path):
    os.remove(path)
else:
    print('파일이 없습니다.')

#
# if os.path.isdir('test'):
#     print('폴더가 존재합니다.')
# else:
#     os.mkdir('test')

# isdir(), exists()
# if not os.path.isdir('test'): os.mkdir('test')
if not os.path.exists('test'): os.mkdir('test')

#현재 폴더에서 파이썬 파일의 목록과 파일의 크기 출력
import os
#현재디렉토리내의 파일명, 사이즈 구하기
print(os.listdir())
for flist in os.listdir():
     print(flist, os.path.getsize(flist))

#특정 디렉토리내의 파일명, 사이즈 구하기 scandir
print('-----------------------')
for flist in os.scandir('c:\\Temp'):
     print(flist.name, os.path.getsize(flist))

print('-----------------------')
print(os.listdir())
for flist1 in os.listdir():
    if os.path.isfile(flist1):
     print(flist1, os.path.getsize(flist1))

# os.path.dirname(), os.path.basename()
import os
mypath = r'c:\temp\hello.py'
print(os.path.dirname(mypath)) # 전체경로에서 디렉토리만 출력
print(os.path.basename(mypath)) # 전체경로에서 파일명만 출력

#
import shutil
#os.mkdir(r'c:\temp2')
old_path = 'c:\\temp\\hello.py'
new_path = 'c:\\temp2\\hello.py'
#shutil.move(old_path,new_path) #파일 이동
shutil.copy(new_path,r'c:\Temp\hello2.py') #파일 복사
