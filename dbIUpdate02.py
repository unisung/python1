import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

name=input('수정할이름:')
phone=input('phone:')
addr=input('addr:')

sql=f'select * from tblAddr where name=\'{name}\''

print(sql)
cursor.execute(sql)
record=cursor.fetchone()

print(record)
namedb=record[0]
phonedb=record[1] if phone=='' else phone
addrdb=record[2] if addr=='' else addr

print(namedb,phonedb,addrdb)

sql_update=f'update tblAddr set phone=\'{phonedb}\',addr =\'{addrdb}\' where name=\'{namedb}\''
print(sql_update)
cursor.execute(sql_update)
con.commit()

cursor.execute(f'select * from tblAddr where name=\'{name}\'')
record=cursor.fetchone()
print('이름:%s, 전화:%s, 주소:%s ' % record)

cursor.close()
con.close()
