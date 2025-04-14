import sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()
res = dbcursor.execute('select * from tel order by id')


name = input("수정할 이름 입력:")
tel = input("전화번호:")
addr = input("주소")
memo = input("메모")

result = dbcursor.execute("update tel set tel = ?, addr = ?, memo = ? where name = ?", (tel,addr,memo,name))

if result.rowcount > 0:
    print("Update successful")
else:
    print("No rows were updated")

dbconn.commit()
#
# if flag == 0:
#     print('\n수정 실패!!\n')
# else:
#     print('\n수정 성공!!\n')
