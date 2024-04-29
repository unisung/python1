#2. 파일 취합
import os
file_path=r'c:\파일\data\quiz1'
f=open('data1.txt','w')
os.chdir(file_path)# 디렉토리 이동처리
flist=os.listdir() # 이동한 현재 디렉토리내의 파일리스트
for fname in flist:
    read_file = open(fname,'r',encoding='cp949')
    #print(read_file.read())
    f.write(read_file.read()) #readline,readlines,read
    read_file.close()
f.close()




