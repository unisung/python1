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

