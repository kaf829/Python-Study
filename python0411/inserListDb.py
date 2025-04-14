import sqlite3
import time

dbconn =sqlite3.connect("tel.db")
dbcursor = dbconn.cursor()



data =[
('Alice', '010-1234-5678', 'Seoul', time.asctime(time.localtime(time.time())), 'Friend from school'),
 ('Bob', '010-2345-6789', 'Busan', time.asctime(time.localtime(time.time())), 'Colleague'),
('Charlie', '010-3456-7890', 'Incheon', time.asctime(time.localtime(time.time())), 'Gym buddy'),
('David', '010-4567-8901', 'Daegu', time.asctime(time.localtime(time.time())), 'Neighbor'),
('Eve', '010-5678-9012', 'Daejeon', time.asctime(time.localtime(time.time())), 'Cousin'),
('Frank', '010-6789-0123', 'Gwangju', time.asctime(time.localtime(time.time())), 'Book club member'),
('Grace', '010-7890-1234', 'Ulsan', time.asctime(time.localtime(time.time())), 'Yoga instructor'),
('Hank', '010-8901-2345', 'Suwon', time.asctime(time.localtime(time.time())), 'Old friend'),
('Ivy', '010-9012-3456', 'Jeju', time.asctime(time.localtime(time.time())), 'Travel buddy'),
('Jack', '010-0123-4567', 'Gyeongju', time.asctime(time.localtime(time.time())), 'Classmate')
]



sql = "insert into tel (name, tel, addr, input_time ,memo) values (?,?,?,?,?)"
dbcursor.executemany(sql,data)

dbconn.commit()

for row in dbcursor.execute('select * from tel'):
    print(row)

dbcursor.close()
dbconn.close()

