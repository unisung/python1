import pymysql

con = pymysql.connect(host='127.0.0.1',user='root', password='1234',db='addr', charset='utf8') # Database 생성 및 연결
cursor = con.cursor() #Database 연결 객체 생성
#SQL명령문 실행
cursor.execute("drop table if exists tblAddr")
cursor.execute("""create table tblAddr
(name char(16) primary key, phone char(16), addr text)
""")
#
cursor.execute("insert into tblAddr values ('김상형','010-1123-5678','오산')")
cursor.execute("insert into tblAddr values ('한경은','010-1124-6678','수원')")
cursor.execute("insert into tblAddr values ('한주완','010-1125-7678','대전')")
cursor.execute("insert into tblAddr values ('홍길동','010-2125-1678','광주')")

#DB반영처리
con.commit()

cursor.close()
con.close()
print("저장완료")