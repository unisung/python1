#함수
#1.매개변수 받고 결과를 리턴하는 형태
def fun1(name):
    return "hello" +name

#2.매개변수 받고 결과를 리턴하지않는 형태
def fun2(name):
    print("hello"+name)

#3.매개변수 안받고 결과를 리턴하는 형태
def fun3():
    return "hello everyone~!!"

#4.매개변수 안받고 결과를 리턴하지않는 형태
def fun4():
    print("hi bye me!")

#함수실행하기
result = fun1('홍길동')
print(result)
fun2('일지매')
result2=fun3()
print(result2)
fun4()

#내장 함수
engt="python programming"
kot="파이썬 프로그래밍"
pro=["OA","Prog","Multi","Prog"]
print("len:",len(engt),len(kot), len(pro))
print("count:",engt.count("p"), kot.count("파"), pro.count("Prog"))
print("index:",engt.index('h'), pro.index('OA'))
#print("index:",engt.find('h'), pro.find('OA')) #list에는 find가 없음
print(dir([]))
#
print("index:",engt.find('k')) # 해당객체없으면 -1리턴
#print("index:",engt.index('k')) # 해당객체없으면 Value Error리턴

#문자열
prog="java c++ Python html5"
print(prog.upper())
print(prog.lower())
print(prog.istitle())
res=prog.replace("c++","GO")
print(res)
print(prog)

#문자열 연결
text="123abc가나다"
prog=["java","c++","python","html5"]
print("-".join(text))
print(", ".join(prog)) #"java, c++, python, html5"

#문자분리
t1='java py html'
t2='java/py/html'
print(t1.split()) #리스트형태로 출력
print(t2.split('/'))

#공백제거
t="  korea   123  "
print(len(t),t)
print(len(t.lstrip()), t.lstrip())
print(len(t.rstrip()), t.rstrip())
print(len(t.strip()), t.strip())

# ord(문자), chr(숫자)
for a in range(65,91):
    print(chr(a),end='')

