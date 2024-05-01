import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

con.execute('select * from tblAddr')
table=cursor.fetchall()
for record in table:
    print('이름:%s, 전화:%s, 주소:%s ' % record)

cursor.close()
con.close()