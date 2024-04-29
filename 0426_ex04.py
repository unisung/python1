#파일목록에 없는 내용 추출
#광주1호선.txt 내용을 리스트형태로 저장
#지하철폴더 파일목록 리스트형태로 저장
#list1과 list2 내용 비교 중복되 내용이있으면 list1에서 삭제
#list1에 남은 내용은 지하철 폴덩에 없는 파일.
#미제출.txt로 저장
import os
def Only_Data2(mylist, del_txt):
    for a in range(len(mylist)):
        mylist[a]=mylist[a].replace(del_txt,'')
    return mylist

file_path=r'C:\파일\data\quiz4'
subway = Only_Data2(os.listdir(file_path+'\지하철'),'.csv')

for i in range(len(subway)):
    subway[i]=subway[i].replace('.csv','')
print(subway)
kwangju=[]
with open(file_path+'\광주1호선.txt','r',encoding='utf-8') as f:
    kwangju=Only_Data2(f.readlines(),'\n')

print('kwangju:',kwangju)
for station in subway:
    if station in kwangju:
        kwangju.remove(station) # 리스트.remove(객체), ['평동','도산',..'광주송정']
print(kwangju)
with open('미제출.txt','w') as f2:
    f2.write('\n'.join(kwangju))


