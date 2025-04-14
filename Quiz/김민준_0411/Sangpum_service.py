from Quiz.김민준_0411.Sanpum_dao import Db_Connection
from Quiz.김민준_0411.User_Exception import User_Exception

class Sangpum_service:
    def __init__(self):
        self.code = ""
        self.irum = ""
        self.su = 0
        self.danga = 0
        self.kumack = 0

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def __str__(self):
        return (f"코드: {self.code}, 이름: {self.irum}, 수량: {self.su}, "
                f"단가: {self.danga}, 금액: {self.kumack}")

    def input_sangpum(self, key=""):
        try:
            if not key:
                self.code = input("코드를 입력하세요: ")

            self.irum = input("이름을 입력하세요: ")
            try:
                self.su = int(input("수량을 입력하세요: "))
                self.danga = int(input("단가를 입력하세요: "))
                self.kumack = self.su * self.danga
                if not (self.su >= 0 and self.danga >= 0):
                    raise User_Exception("수량과 단가는 0 이상이어야 합니다", 2)
            except ValueError:
                raise User_Exception("수량과 단가는 숫자여야 합니다", 2)
        except User_Exception as e:
            return print(e)

    @classmethod
    def input_data(cls):
        try:
            item = Sangpum_service()
            item.input_sangpum()
            connection = Db_Connection()

            print(item)
            connection.dbconnection("INSERT", item.code, item.irum, item.su, item.danga, item.kumack, code=item.code)
        except User_Exception as e:
            print(e)

    @classmethod
    def output_data(cls):
        connection = Db_Connection()
        selectByAll = connection.dbconnection("SELECT")
        selectCount = connection.dbconnection("COUNT")
        sum = 0
        print(selectCount)
        print("\n                      *** 상품 목록 ***")
        print("============================================================")
        print("코드 \t   이름  \t  수량  \t  단가  \t  금액")
        for row in selectByAll:
            sum += row[4]
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[2],"\t",row[4])
        print("============================================================")
        print(f"\t\t 총상품수 = {selectCount[0]},  전체 금액 = {sum:.2f}\n")

    def search_data(self):
        code = input("\n조회할 코드를 입력하세요: ")
        connection = Db_Connection()
        row = connection.dbconnection("SELECTBYONE", code, code=code)
        print("============================================================")
        print("코드 \t   이름  \t  수량  \t  단가  \t  금액")
        print("============================================================")
        print(row[0],"\t",row[1],"\t",row[2],"\t",row[2],"\t",row[4])

    def modify_data(self):
        code = input("\n수정할 코드를 입력하세요: ")
        item = Sangpum_service()
        item.set_code(code)
        item.input_sangpum("modify")
        connection = Db_Connection()

        print(item)
        connection.dbconnection("UPDATE", item.irum, item.su, item.danga, item.kumack, item.code, code=code)

    def delete_data(self):
        code = input("\n삭제할 코드를 입력하세요: ")
        item = Sangpum_service()
        item.set_code(code)
        connection = Db_Connection()
        print(item)
        connection.dbconnection("DELETE", item.code, code=code)
