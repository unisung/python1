'''
addr.db 디비에저장된
명단의 리스트 중 phone 혹은 addr을 수정하는 코드작성
name=input('수정할이름:')
phone=input('phone:')
addr=input('addr:')
update tblAddr set phone=phone, addr=addr where name=name
commit
수정된 내용 조회
select * from tblAddr where name=name
'''
