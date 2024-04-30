#pip - python install package
# pip install 패키지명 -설치
# pip install 패키지명==버전 -특정버전으로 설치
# pip uninstall 패키지명 - 제거
# pip install --upgrade 패키지명 - 업그레이드
# pip list #설치된 패키지 목록 조회

# Faker 가짜 데이타 생성
#pip install Faker
from faker import Faker
faker=Faker()
print(faker.name())
print(faker.address())
faker=Faker('ko-KR')
print(faker.name())
print(faker.address())
test_data=[(faker.name(), faker.address()) for i in range(30)]
print(test_data)
print(faker.postcode())
print(faker.country())
print(faker.company())
print(faker.job())
print(faker.phone_number())
print(faker.email())
print(faker.user_name())
print(faker.pyint(min_value=0, max_value=100))
print(faker.ipv4_private())
print(faker.text())
print(faker.color_name())

#방정식 기호 출력
from fractions import Fraction
import sympy
# 가지고 있던 돈을 x라고 하자.
x = sympy.symbols("x")

# 가지고 있던 돈의 2/5가 1760원이므로 방정식은 x * (2/5) = 1760 이다.
f = sympy.Eq(x*Fraction('2/5'), 1760)

# 방정식을 만족하는 값(result)을 구한다.
result = sympy.solve(f)  # 결괏값은 리스트

# 남은 돈은 다음과 같이 가지고 있던 돈에서 1760원을 빼면 된다.
remains = result[0] - 1760

print('남은 돈은 {}원 입니다.'.format(remains))