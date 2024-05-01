import sqlite3

con = sqlite3.connect('addr2.db') # Database 생성 및 연결
cursor = con.cursor() #Database 연결 객체 생성
#SQL명령문 실행
cursor.execute("drop table if exists myAddr")
cursor.execute("""create table myAddr
(name char(20) primary key, phone char(20), addr text,
 info text)
""")

for i in range(3):
    print('정보를 입력하세요=>')
    name = input('name:')
    phone = input('phone:')
    addr = input('주소:')
    info = input('메모:')
    sql=f"insert into myAddr values (\'{name}\',\'{phone}\',\'{addr}\',\'{info}\')"
    cursor.execute(sql)

#DB반영처리
con.commit()

cursor.close()
con.close()
print("저장완료")