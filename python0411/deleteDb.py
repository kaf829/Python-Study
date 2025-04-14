import sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()
res = dbcursor.execute('select * from tel order by id')


memo = input("삭제할 메모 입력:")

result = dbcursor.execute("Delete from tel where memo = ?", (memo,))


print(result.rowcount)

if result.rowcount > 0:
    print("데이터 삭제 성공")
else:
    print("데이터 삭제 실패")

dbconn.commit()
#
# if flag == 0:
#     print('\n수정 실패!!\n')
# else:
#     print('\n수정 성공!!\n')
