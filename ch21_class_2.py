# class
# 필드, 메소드, 생성자, camel방식 선언
class MyClass: #클래스 키워드 class 클래스명:
    pass

#first와 second 두개의 인스턴스 필드를 가진 클래스 생성
class Calc:
    def __init__(self):
        pass
    def __init__(self,first,second): #인스턴스 자신 가리킴
        self.first=first
        self.second=second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

#객체 생성
a=Calc(10,20)
#a=Calc()
print(a.add())

#상속
class MyClass(Calc):
    pass

b=MyClass(10,20)
print(b.add())
print(b.sub())
print(b.mul())
print(b.div())

b=MyClass(10,0)
#print(b.div())

# 오버라이드
class SafeCalc(Calc):
    def div(self): # 자식클래스에서 부모메소드 재정의
        if self.second==0:
            return 0
        return self.first / self.second

    def setdata(self,first,second):
        self.first=first
        self.second=second

c=SafeCalc(10,0)
print(c.div())
c.setdata(10,20)
print(c.div())







