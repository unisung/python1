#리스트
# f=[] #빈 리스트
# a=[90,92,84,88,74] #표기법[]
# b=list((90,92,84,88,74)) #list()함수
# c=["파이썬",[900, 30.5, "자바"],850,78.75]
# d=list(("파이썬",900, 30.5, "자바",850,78.75))
# e=list("프로그래밍") #문자열 -> 리스트
# print(a,b,c,d,e,f,sep="\n")

#인덱싱(해당index의 값 추출),
# 슬라이싱(특정 index범위의 값 추출)
#a=[90,91,92,93,94,95,96]
# a=list(range(90,97))
# print(a[0]) # [0,1,2,3,4,5,6] [0,...len-1]
# print(a[-1]) #[-7,-6,-5,-4,-3,-2,-1] [-len,...,-1]
# print(a[-7])
#
# #
# print(a[0:3]) # 0<=범위<3 => 0,1,2
# print(a[3:5])
# print(a[0:]) # 0<=범위<끝길이(전체)
# print(a[:]) # 0<=범위<끝길이(전체)
# print(a[3:]) # 3<=범위<끝길이
# #a[시작:끝:증분]
# print(a[1:5:2])
# print(a[::2]) # 전체 인덱스 0부터 2씩증가
# print(a[1::2]) # 1<=범위<끝길이, 2씩증가
# print(a[-4:-2]) # -4<=범위<-2
# print(a[-4:])
# #print(a[100]) # 범위를 벗어난 indexing
#  # IndexError: list index out of range
# print(a[5:100]) # 해당 index범위까지만 출력
#
# # 문자열 indexing
# ct = '프로그래밍'
# print(ct[1],ct[-1])
#
# #리스트 연산 - 항목수정
# prog=["C","PYTHON","JAVA","GO"]
# prog[0]="C++"
# print(prog)
#
# #리스트 복사
# prog=["C","PYTHON","JAVA"]
# myprog=prog
# print("prog",prog)
# print("muyprog",myprog)
# prog[0]="C++"
# print("prog",prog)
# print("muyprog",myprog)
#
# #깊은 복사 deep copy
# prog=["C","PYTHON","JAVA"]
# #myprog=[]
# #for a in prog:
# #    myprog.append(a)
# myprog=[a for a in prog]
# print("prog",prog)
# print("muyprog",myprog)
# prog[0]="C++"
# print("prog",prog)
# print("muyprog",myprog)

#리스트 연산
# prog=["C","PYTHON","JAVA","GO"]
# webp=["PHP","JSP","ASP.NET"]
# myprog=prog+webp # 새로운 리스트 객체 생성
# prog[0] = 'D'
# print("prog:",prog)
# print("myprog:",myprog)

#타입 오류
# prog=["C","PYTHON","JAVA","GO"]
# myprog = prog +"HTML" #TypeError: can only concatenate list (not "str") to list
#=>
# prog=["C","PYTHON","JAVA","GO"]
# myprog = prog +["HTML"] # 리스트 +리스트 =>새로운 객체생성

#리스트 반복 *
# prog=["C","PYTHON","JAVA"]
# data=[1,2,3]
# print(prog*2) #새로운 객체 생성
# print(data*3) #새로운 객체 생성

# 리스트 메소드들...
# index
# print(dir([1,2,3])) #dir(객체) 메소드 리스트 출력
# prog=["C","PYTHON","JAVA","GO","PYTHON"]
# print(prog.index('PYTHON')) # 리스트상 해당하는 객체의 첫번째index
# #print(prog.index('PHP')) # 리스트내에 없으면 오류 발생
# print(prog.index("python")) #대소 문자 구분함

# append, extend, insert
# 뒤에 이어붙이기
a=[1,2,3,4]
b=["WEB","OA","Multi"]
a.append(5)
a.append("python")
a.append([6,7])
a.append(b)
print(a)

