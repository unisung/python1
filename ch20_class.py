#클래스
# class 클래스명:
#     속성....

class FourCal:
    pass

# 변수 = 클래스명() #default생성자
a=FourCal()
print(type(a))

#def setdata(first,second):

class FourCal:
    #생성자 __init__ # 생성된 객체의 변수 초기화
    def __init__(self,first,second):
        self.first = first
        self.second = second
    #def __init__(self):
    #    pass
    def setdata(self,first,second):
        self.first=first
        self.second=second

    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        return self.first * self.second
    def sub(self):
        return self.first - self.second
    def div(self):
        return self.first / self.second

#a=FourCal()
a=FourCal(10,20) #
a.setdata(10,20)
print(a.first, a.second)
print(a.add(), a.mul(),a.sub(),a.div())


#클래스 상속
#class 자식클래스(부모클래스):
class MoreFourCal(FourCal):
    pass

b=MoreFourCal(4,2)
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

#상속후 추가
class MoreFourCal(FourCal):
    def pow(self):
        return self.first**self.second

c=MoreFourCal(4,3)
print(c.pow())


#메소드 오버라이딩, 오버로딩
#상속받은 메소드의 내용부분을 재정의
class SafeFourCal(FourCal):
    def div(self,first,second):
        if self.second ==0:
            return 0
        else:
            return self.first / self.second
    def div(self):
        if self.second ==0:
            return 0
        else:
            return self.first / self.second

    def _mul_(self):
        return self.first * self.second

#SafeFourcal={'div':function(), 'div':function(f,s)}

c=SafeFourCal(10,0)
print(c.div())
c=SafeFourCal(10,3)
print(c.div())
print(c.div())
print('--------')
print(c._mul_())

#추상클래스
from abc import *
class AbsClass(metaclass=ABCMeta):
    @abstractmethod
    def myab(self):
        pass

class BBB(AbsClass):
    def myab(self): # 추상메소드 재정의
        pass
#k=AbsClass()
k=BBB()









