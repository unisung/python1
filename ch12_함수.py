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
