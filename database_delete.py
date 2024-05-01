import sqlite3
#database연결
con=sqlite3.connect('addr.db')
#db연결객체 생성
cursor = con.cursor()
#sql문
sql=f'delete from tblAddr where name=\'홍길동\''
print(sql)
#sql문 실행
cursor.execute(sql)
#db저장
con.commit()


#커서객체 해제
cursor.close()
#연결해제
con.close()