import sqlite3
#database연결
con=sqlite3.connect('addr.db')
#db연결객체 생성
cursor = con.cursor()

name=input('삭제할 이름을 입력하세요:')
isdelete=input('정말삭제하시겠습니까?(y/n)')
if isdelete=='y':
#sql문
    sql=f'delete from tblAddr where name=\'{name}\''
    print(sql)
#sql문 실행
    cursor.execute(sql)
#db저장
    con.commit()
else:
    print('취소하셨습니다.')

cursor.execute(f'select * from tblAddr')
table=cursor.fetchall()
for record in table:
    print('%s, %s, %s'%record)

#커서객체 해제
cursor.close()
#연결해제
con.close()