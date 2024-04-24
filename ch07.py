#while문
'''
login = True

while login:
    pw = input('pw')
    if pw=="test":
        login =False
        print("접속성공")
    else:
        print("비밀번호 오류!")
'''
# id/ pwd 입력 "admin", "test" 둘다맞으면 접속성공
# id가 틀리면 "id오류",  "비번오류"
# while문으로 작성

login = True
while login:
    id =input("ID:")
    pw =input("PW:")
    if id=="admin": #id가admin이라면
        if pw=="test":#pw가test라면
            login = False
            print("Hello")
        else: #id는일치하지만비밀번호가틀린경우
            print("WrongPW")
    else: #id가admin이아닌경우
        print("WrongID")