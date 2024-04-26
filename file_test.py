import random

data = "00000000"

ascii_str1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
ascii_str2 = ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ascii_str3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
ascii_str4 = ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for t in range(1, 11):

    rand_str1 = random.choice(ascii_str1)
    rand_str2 = random.choice(ascii_str2)
    rand_str3 = random.choice(ascii_str3)
    rand_str4 = random.choice(ascii_str4)

    filename = "c:\\Temp\\quiz1\\" + rand_str1 + rand_str2 + rand_str3 + rand_str4 +"%d.txt" % t

    print(filename)
    f = open(filename, 'a+')
    f.write('이름:홍길동\n')
    f.write('생년월일:1980.03.18\n')
    f.write('전자우편:singer@gmail.com\n')
    f.write('휴대폰:010-1666-4889\n')

    data = ""

    f.close()

