#select문
import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute('select * from tblAddr')
#table = cursor.fetchall() # 전체 record조회
#table = cursor.fetchone() # 한건 조회
table = cursor.fetchmany(6) # n건 조회, 저장데이터 건수보다 n이 크면 저장건수출력
for record in table:
    print('이름:%s, 전화:%s, 주소:%s'% record)

cursor.close()
con.close()

