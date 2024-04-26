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

a=FourCal()
a.setdata(10,20)
print(a.first, a.second)
print(a.add(), a.mul(),a.sub(),a.div())



