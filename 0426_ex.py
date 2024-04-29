#quiz1. 파일 이름 변경하기
import os
#file_list = os.listdir(r'c:\파일\data\quiz1') #디렉토리내의 파일만출력
file_path=r'c:\파일\data\quiz1'
file_list = os.scandir(file_path) # 경로+파일

for fname in file_list:
    with open(fname, 'r') as f:
        data=f.readline().replace('\n','')
        data=data.split(':') #['이름','홍길동']
        re_file=os.path.join(file_path, f'{data[-1]}.txt')
    os.rename(fname, re_file)


