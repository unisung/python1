# #예외처리
# #f=open("없는파일",'r')
# #4/0
# #a=[1,2,3]
# #a[3]
#
# # try-except 문
# #1. try-except문만 사용
# try:
#     4/0
# except:
#     print('오류발생')
#
# #2.발생오류만 포함하는 except문
# try:
#     4/0
# except ZeroDivisionError:
#     print('오류발생')
#
# #3.발생오류와 오류변수까지 포함한 except문
# try:
#     4/0
# except ZeroDivisionError as e: # e=ZeroDivisionError()
#     print(e) # 객체참조변수가 print()문의 매개변수로 전달되면 __str__()메소드가 자동호출됨.
#
# # try-finally 문
# try:
#     f=open('foo.txt','w')
#     data=f.read()
#     print(data)
#
# finally: #try:문에서 정상이든, 에러가 발생하든 상관없이 종료전에 실행.
#     f.close()
#     print('파일닫기')

#여러개 예외 처리
# try:
#     a=[1,2]
#     print(a[3]) # index오류
#     4/0  # 0으로 나눈 오류
# except ZeroDivisionError:
#     print("0으로 나눌수 없습니다.")
# except IndexError:
#     print("인덱싱 할수 없습니다.")
#
# finally:
#     print('종료!!!!')
# # as
# try:
#     a=[1,2]
#     print(a[3]) # index오류
#     4/0  # 0으로 나눈 오류
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)
#
# finally:
#     print('종료!!!!')
#
# # except예외 같이 사용
# try:
#     a=[1,2]
#     print(a[3]) # index오류
#     4/0  # 0으로 나눈 오류
# except (ZeroDivisionError,IndexError) as e: #(예외객체나열) as e
#     print(e)
#
# finally:
#     print('종료!!!!')
#
# #try~else문
# try:
#     age=int(input('나이를 입력하세요:'))
# except:
#     print("입력이 정확하지않음")
# else: #오류가 없으면 실행하는 문장
#     if age<=18:
#         print('미성년자 출금')
#     else:
#         print('환영합니다.')
#
#
#  #오류발생시 지나가기
# try:
#      f=open('없는파일.txt','r')
# except FileNotFoundError:
#      pass

#오류 강제발생
class Bird: #새 추상적 개념
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()

# 사용자 정의 예외 만들기
class MyError(Exception):
    pass

def say_nick(nick):
    if nick=='바보':
        raise MyError()
    print(nick)

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    #print('허용되지않는 별명입니다.')
    print(e)

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)
class MyError2(Exception):
    def __str__(self):
        return "출금액이 잔고보다 큽니다."
class Account:
    def __init__(self,accountNo, owner, balance):
        self.accountNo=accountNo
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance +=amount

    def withdraw(self,amount):
        if self.balance - amount < 0:
            raise MyError2
        self.balance -=amount

    def getbalance(self):
        return self.balance

    def __str__(self):
        return ('계좌번호:'+self.accountNo+', 소유자:'
                + self.owner + ' 잔고:'+str(self.balance))

acc1 = Account('a10117','홍길동',10000)
try:
    print(acc1.getbalance())
    print(acc1)
    acc1.deposit(10000)
    print(acc1)
    acc1.withdraw(50000)
except MyError2 as e:
    print(e)
print(acc1)

# 상품재고클래스 생성
# 상품코드 8801123, '새우깡', 재고 100
# 재고 없을시 StockError 예외 발생 '재고가 없습니다'
# 입고: 50, 입고 20, 출고 200시 예외발생후 이전 재고량출력
class Stock:
    #itemcode, name, qty
    #입고 deposit()
    #출고 withdraw()
    #__str__()
    #입/출고량 amount


