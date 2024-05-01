#select문
import pymysql

con = pymysql.connect(host='43.203.231.53',user='root',
                      password='1234',
                      db='yhs', charset='utf8') # Database 생성 및 연결
cursor = con.cursor()

name=input('조회할 이름:')
sql=f'select * from tblAddr where name=\'{name}\''
print('sql:',sql)
#쿼리문 실행
cursor.execute(sql)
record=cursor.fetchone()
print('이름:%s, 전화:%s, 주소:%s'% record)

cursor.close()
con.close()

