import mod1 # 동일 패키지에서 다른 모듈 임포트
print(mod1.sub(10,20)) # 모듈명.함수()
print(mod1.add(10,20))

from mod1 import add, sub # from 모듈 import 함수
print(add(10,20)) # 함수()
print(sub(10,20))

from mod1 import * # from 모듈 import 함수 wildcard문자 '*'
print(add(10,20)) # 함수()
print(sub(10,20))

