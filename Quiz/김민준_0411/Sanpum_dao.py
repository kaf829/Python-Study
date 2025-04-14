import sqlite3

from Quiz.김민준_0411.User_Exception import User_Exception


class Db_Connection:
    def __init__(self):
        pass

    def dbconnection(self, dml, *args, code=""):
        try:
            result = ''
            dbconn = sqlite3.connect('sangpum.db')
            dbcursor = dbconn.cursor()

            if dml not in ["SELECT", "SELECTBYONE"]:
                try:
                    result = dbcursor.execute(self.dml_query("TRANSATION"), (code,))
                    if dml in ["UPDATE","DELETE"] and (type(result.fetchone()) == tuple):
                        print("해당 품번이 존재하여 품목을 수정/삭제 하겠습니다")
                    else:
                        result = dbcursor.execute(self.dml_query("TRANSATION"), (code,))
                        if (result.fetchone() is not None) or (type(result.fetchone()) == tuple):
                            raise User_Exception(f"{args}", 3)
                except Exception:
                    raise User_Exception(f"{args}", 3)

            query_result = dbcursor.execute(self.dml_query(dml), args)

            dbconn.commit()

            if dml == "SELECT":
                result = query_result.fetchall()
            else:
                result = query_result.fetchone()

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
        elif dml == "COUNT":
            return "SELECT COUNT(*) FROM SANGPUM"
