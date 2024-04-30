#클로저 - inner-function을 포함하는 함수
# def mul3(n):
#     return n*3
# def mul5(n):
#     return n*5
# # 2,4,7,...
#
# class Mul:
#     def __init__(self,m):
#         self.m=m
#
#     def mul(self,n):
#         return self.m*n
#
# mul3=Mul(3)
# mul5=Mul(5)
# print(mul3.mul(10))
# print(mul5.mul(5))
#
#
# class Mul:
#     def __init__(self,m):
#         self.m=m
#
#     def __call__(self, n):
#         return self.m*n
#
#     #def mul(self,n):
#     #    return self.m*n
#
# mul3=Mul(3)
# mul5=Mul(5)
# print(mul3(10))
# print(mul5(5))
#
# def mul(m): # outer-function
#     def wrapper(n): # inner-function
#         return m*n
#     return wrapper
#
# mul3=mul(3)
# mul5=mul(5)
#
# print(mul3(10))
# print(mul5(10))
#
# #데코레이터
# import time
# def myfunc():
#     start=time.time()
#     print("함수가 실행됩니다.")
#     end = time.time()
#     print("함수 수행시간: %f 초" %(end-start))
#
# myfunc()
#

import time

def elapsed(original_func):
    def wrapper():
        start = time.time()
        result = original_func() # 함수실행
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
        return result
    return wrapper

@elapsed #데코레이터 패턴
def myfunc():
    print("함수실행됩니다.")

#decorated_myfunc = elapsed(myfunc) #함수명을 매개변수로 전달
#decorated_myfunc()
myfunc()


def elapsed2(original_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs) # 함수실행
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
        return result
    return wrapper

@elapsed #데코레이터 패턴
def myfunc():
    print("함수실행됩니다.")

myfunc()
@elapsed2
def myfunc2(msg):
    print("'%s'을 출력합니다."%msg)

myfunc2("You need python")


from abc import *
class AbsrtactCountry(metaclass=ABCMeta):
    name='국가명'
    population='인구'
    capital='수도'
    def show(self):
        print('클래스메소드')

    @abstractmethod
    def show_capital(self):
        print('국가의 수도')

#a=AbsrtactCountry()

class Korean(AbsrtactCountry):
    def __init__(self,name, population,capital):
        self.name=name,
        self.population=population
        self.capital=capital

    def show_capital(self):
        super().show_capital()
        print(self.capital)

a=Korean('대한민국',5000000, '서울')


# @classmethod, @staticmethod
class CustomClass:
    def add_instance_method(self,a,b):
        return a+b

    @classmethod # 클래스에 소속된메소드
    def add_class_method(cls,a,b):
        return a+b

    @staticmethod #클래스에 소속되지않은 메소드
    def add_static_method(a,b):
        return a+b


print(CustomClass.add_instance_method(None,3,5))
#print(CustomClass.add_class_method(None,3,5))
print(CustomClass.add_static_method(3,5))

a=CustomClass()
print(a.add_class_method(3,5))
print(a.add_static_method(3,5))


# class - 덕 타이핑(Duck Typing)
class Parrot:
    def fly(self):
        print("Parrot flying")

class Airplain:
    def fly(self):
        print("airplain flying")

class Whale:
    def swim(self):
        print("Whale swimming")

def lift_off(entity):
    entity.fly()

parrot = Parrot()
airplane=Airplain()
whale=Whale()

lift_off(parrot)
lift_off(airplane)
#lift_off(whale)

