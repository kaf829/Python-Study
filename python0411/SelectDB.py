import  sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()

print("NO \t 성명 \t 전화번호 \t 주소 \t 메모 \t 입력일자")
print("-" * 100)

for row in dbcursor.execute("SELECT * FROM TEL ORDER BY ID"):
    print(str(row[0])+"\t"+str(row[1])+"\t"+str(row[2])+"\t"+str(row[3])+"\t"+str(row[5])+"\t"+str(row[4]))
    print("-"*100)


dbcursor.close()
dbconn.close()