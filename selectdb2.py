#select문
import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

name=input('조회할 이름:')
sql=f'select * from tblAddr where name=\'{name}\''
print('sql:',sql)
#쿼리문 실행
cursor.execute(sql)
record=cursor.fetchone()
print('이름:%s, 전화:%s, 주소:%s'% record)
# while True:
#     record = cursor.fetchone()
#     if record == None:
#         break
#     print('이름:%s, 전화:%s, 주소:%s'% record)
cursor.close()
con.close()

