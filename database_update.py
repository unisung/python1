import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute('update tblAddr set addr =\'제주도\' where name=\'김상형\'')
con.commit()

cursor.execute('select * from tblAddr where name=\'김상형\'')
record=cursor.fetchone()
print('이름:%s, 전화:%s, 주소:%s ' % record)

cursor.close()
con.close()

