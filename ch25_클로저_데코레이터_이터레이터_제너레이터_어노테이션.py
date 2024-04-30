#클로저 - inner-function을 포함하는 함수
def mul3(n):
    return n*3
def mul5(n):
    return n*5
# 2,4,7,...

class Mul:
    def __init__(self,m):
        self.m=m

    def mul(self,n):
        return self.m*n

mul3=Mul(3)
mul5=Mul(5)
print(mul3.mul(10))
print(mul5.mul(5))


class Mul:
    def __init__(self,m):
        self.m=m

    def __call__(self, n):
        return self.m*n

    #def mul(self,n):
    #    return self.m*n

mul3=Mul(3)
mul5=Mul(5)
print(mul3(10))
print(mul5(5))

def mul(m): # outer-function
    def wrapper(n): # inner-function
        return m*n
    return wrapper

mul3=mul(3)
mul5=mul(5)

print(mul3(10))
print(mul5(10))

#데코레이터
import time
def myfunc():
    start=time.time()
    print("함수가 실행됩니다.")
    end = time.time()
    print("함수 수행시간: %f 초" %(end-start))

myfunc()


import time

def elapsed(original_func):
    def wrapper():
        start = time.time()
        result = original_func() # 함수실행
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
        return result
    return wrapper

def myfunc():
    print("함수실행됩니다.")

decorated_myfunc = elapsed(myfunc) #함수명을 매개변수로 전달
decorated_myfunc()






