#정규표현식
data = """
park 800905-1049118
kim  700905-1059119
"""

result=[]
for i, line in enumerate(data.split("\n")):
    print(i,line)
    word_result=[]
    for word in line.split(" "):
        print(word)
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" +"*******"
        word_result.append(word)
    result.append(" ".join(word_result))

print("\n".join(result))

# 정규표현식으로 처리
#1. 정규표현식 모듈 import
import re
data = """
park 800905-1049118
kim  700905-1059119
"""
#2.정규표현식처리 객체 생성
pat = re.compile("(\\d{6})[-]\\d{7}") # "\d" <= "\\d"
#3. 처리/변환
print(pat.sub("\\g<1>-*******",data))

#메타문자들 : . ^ $ * + ? { } [ ] \ | ( )
# [] -문자하나 [abc] <- a하나, 혹은 b하나, 혹은 c하나
#[0-5] - 0,1,2,3,4,5 중 하나, [a-z] a~z문자 중 하나
#[0-9] - 모든숫자
#[a-zA-Z] - 모든 알파벳

# . 모든문자  a.b => aab, a0b, abb, abc(x)

# * 갯수 - 0~무한대=> ca*t ct(a가0번), cat(a가 1번반복), caaaaat(a가 여러번반복)

# + 갯수 - 1~무한대=> ca+t ct(X a가0번), cat(a가 1번반복), caaaaat(a가 여러번반복)

# {} 갯수 {n}, {m,}최소m개이상, {,n}최대m개이상  {m,n} 최소m~최대n \d{3}-\d{3,4}-\d{4}
# ca{2,5}t => ct(x), cat(x), caat(o), caaat(o), caaaaaat(x)

# ? 갯수 {0,1} 없거나 1개인 경우 => ab?c => ac(o), abc(o), abbbc(x),
