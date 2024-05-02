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

##정규표현식 이용한 문자열 검색
import re
#match() - 문자열 처음부터 정규식과 매치되는지 조사
# - 패턴에 맞는 값이 없으면 None
p = re.compile('[a-z]+') # a aaa  xx x
data ="python"
m = p.match(data)
print(m)
m=p.match("3 python")
print(m)
##조사결과 None처리
# p=re.compile('[a-z]+')
# inputdata=input('조사할문자열:')
# m=p.match(inputdata)
# if m: #m이 None이 아니면 True
#     print("Match found:", m.group())
# else:
#     print('No match')

#search() - 문자열 전체를 검색하여 정규식과 매치되는지 조사 - None
m = p.search("python")
print(m)
print('-------------')
m=p.search("3 python")
print(m)
#findall() - 정규식과 매치되는 모든 문자열(substring)을 리스트로 반환
result = p.findall("life is too short")
print(result)
#finditer() - 정규식과 매치되는 모든 문자열(substring)을 iterable객체로 반환
result = p.finditer("life is too short")
print(list(result))

##match 메소드
#group() - 매치된 문자열 리턴
#start() - 매치된 문자열 시작 위치
#end() - 매치된 문자열 끝 위치
#span() - 매치된 문자열의 (시작,끝) 위치 튜플로 리턴
m=p.match("python")
print(m.group(), m.start(), m.end(), m.span())

m = p.search("3 python")
print(m.group())

## re.compile() 옵션
# DOTALL(S) - .(dot)이 줄바꿈 문자을 포함해 모든 문자오 매치될 수있게 함.
# IGNORECASE(I) - 대소문자 구분 없이 매치
# MULTILINE(M) - 여러줄과 매칭 되게, ^, $
# VERBOSE(X) - 보기편하게 만듬.
import re
p=re.compile('a.b')
m=p.match('a\nb') #줄바꿈문자 무시
print(m)

p=re.compile('a.b', re.S) #re.DOTALL
m=p.match('a\nb') # 줄바꿈문자 매칭
print(m)

#IGNORECASE, I
p= re.compile('[a-z]+',re.I)
print(p.match('python'))
print(p.match('python'.upper()))
print(p.match('python'.capitalize()))

# MULILINE, M
import re
p=re.compile("^python\\s\\w+", re.MULTILINE) # ^시작

data="""python one
life is too short
python two
you need python
python three"""

print("----------")
print(p.findall(data))

#VERBOSE, X
charref=re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)

# 문자열 소비가 없는 메타 문자
#  | ^ $ \A \Z \b \B
# |
p = re.compile('Crow|Servo')
m=p.match('CrowHello')
print(m.group())

# ^ - starts
print(re.search('^Life','Life is too short'))
print(re.search('^Life', 'My Life'))

#$ - ends
print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))

# \A -줄상관없이 전체 문자열의 처음과 매칭, \Z - 줄상관없이 전체 문자열 마지막

# \b - word boundary
p = re.compile(r'\bclass\b') # \b단어\b 단어 앞뒤로 공백
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass algorithm'))

#\B <= \b와 반대
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass algorithm'))

# 그루핑 (ABC)+
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group())

p=re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search('park 010-1234-1234')
print(m)
print(m.group(0))
# group(인덱스) - group(0) 매칭된 전체문자열, group(1)-첫번재,  group(2)-두번째,,,

p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search('park 010-1234-1234')
print(m.group(0))
print(m.group(1))
print(m.group(2))

p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search('park 010-1234-1234')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))

# 그루핑 문자열 재참조
p = re.compile(r'(\b\w+)\s+\1') # \1 정규식 그룹 중 첫번째 그룹
print(p.search('Paris in the the spring').group())
# (그룹) + " " + 그룹

# 그루핑 문자열에 이름 붙이기
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group())
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group('name'))

#그룹명 재참조
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
print(p.search('Paris in the the spring').group())

#전방탐색 (?=패턴) 긍정형 , (?!패턴) 부정형
p=re.compile('.+:') # http: https:
m=p.search('http://google.com')
print(m.group())

p= re.compile('.+(?=:)')
m=p.search('http://google.com')
print(m.group())

p= re.compile('.*[.](?!bat$).*$')

#sub() - 문자열 변환
p=re.compile('(blue|white|red)')
print(p.sub('colour','blue socks and red socks'))
print(p.sub('colour','blue socks and red socks',count=1))

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\\g<2> \\g<1>", "park 010-1234-1234"))

#sub 메소드의 매개변수로 함수 넣기
def hexrepl(match):
    value=int(match.group())
    return hex(value)

p = re.compile(r'\d+')
print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))

#greedy vs non-greedy
s='<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>',s).span())
print(re.match('<.*>',s).group())
print(re.match('<.*?>',s).group())
