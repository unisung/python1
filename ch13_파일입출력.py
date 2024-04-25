#파일입출력
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

#autocloseable with open() as 별칭:
with open('c:/Temp/pro.txt', 'r') as f:
    t=f.readline()
    print(t)
