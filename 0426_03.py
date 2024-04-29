# 파일 취합 줄단위
import os
file_path=r'c:\파일\data\quiz1'
flist = os.scandir(file_path)
with open('data2.txt', 'w') as f:
    for fname in flist:
        #print(fname)
        with open(fname, 'r') as read_file:
            data=read_file.readlines() #내용 분리
            #print(data)
            for a in range(len(data)):
                data[a]=data[a].replace('\n','')# '\n'제거
                cdata=data[a].split(':') # ['이름','김길동']
                data[a]=cdata[-1]
                print('\t'.join(data),file=f) #파일로 저장
