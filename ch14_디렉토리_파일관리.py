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

#scandir()
file_list = os.scandir()
print(file_list)

for filename in file_list:
    print(filename, filename.name)