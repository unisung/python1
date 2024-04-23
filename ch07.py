#while문
login = True

while login:
    pw = input('pw')
    if pw=="test":
        login =False
        print("접속성공")
    else:
        print("비밀번호 오류!")

# id/ pwd 입력 "admin", "test" 둘다맞으면 접속성공
# id가 틀리면 "id오류",  "비번오류"
# while문으로 작성