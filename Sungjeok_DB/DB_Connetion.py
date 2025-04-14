import sqlite3
from User_Exception import User_Exception

class Db_Connection:
    def __init__(self):
        pass

    def dbconnection(self, dml, *args, code=""):
        try:
            result = ''
            dbconn = sqlite3.connect('sangpum.db')
            dbcursor = dbconn.cursor()

            if dml != "SELECT" or dml != "SELECTBYONE":
                try:
                    result = dbcursor.execute(self.dml_query("TRANSATION"), (code,))

                    if type(result.fetchone()) == tuple:
                        raise User_Exception(f"{args}", 3)

                except Exception:
                    raise User_Exception(f"{args}", 3)

            query_result = dbcursor.execute(self.dml_query(dml), args)

            if dbcursor.rowcount > 0:
                print("데이터 갱신 성공")
            else:
                print("데이터 갱신 실패")

            dbconn.commit()

            if dml == "SELECTBYONE":
                result = query_result.fetchone()
            elif dml == "SELECT":
                result = query_result.fetchall()

            dbcursor.close()
            dbconn.close()

            return result
        except User_Exception as e:
            return print(e)

    def dml_query(self, dml="SELECT"):
        if dml == "SELECT":
            return "SELECT * FROM sangpum"
        elif dml == "INSERT":
            return "INSERT INTO sangpum(code, irum, su, danga, kumack) VALUES (?, ?, ?, ?, ?)"
        elif dml == "UPDATE":
            return "UPDATE sangpum SET irum = ?, su = ?, danga = ?, kumack = ? WHERE code = ?"
        elif dml == "DELETE":
            return "DELETE FROM sangpum WHERE code = ?"
        elif dml == "TRANSATION":
            return "SELECT * FROM sangpum WHERE code = ?"
        elif dml == "SELECTBYONE":
            return "SELECT * FROM sangpum WHERE code = ?"
