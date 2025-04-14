from Sungjeok_DB.DB_Connetion import Db_Connection
from Sungjeok_DB.User_Exception import User_Exception

class Sungjuk:
    def __init__(self):
        self.hakbun = ""
        self.name = ""
        self.korean = 0
        self.math = 0
        self.english = 0
        self.sum_score = 0
        self.avg = 0
        self.grade = ""

    def get_hakbun(self):
        return self.hakbun

    def set_hakbun(self, hakbun):
        self.hakbun = hakbun


    def __str__(self):
        return (f"학번: {self.hakbun}, 이름: {self.name}, 국어: {self.korean}, "
            f"수학: {self.math}, 영어: {self.english}, 총점: {self.sum_score}, "
            f"평균: {self.avg:.2f}, 등급: {self.grade}")

    def input_sungjuk(self, key=""):
        try:
            if not key:
                self.hakbun = input("학번을 입력하세요: ")

            self.name = input("이름을 입력하세요: ")
            try:
                self.korean = int(input("국어 점수를 입력하세요: "))
                self.math = int(input("수학 점수를 입력하세요: "))
                self.english = int(input("영어 점수를 입력하세요: "))
                if not (0 <= self.korean <= 100 and 0 <= self.math <= 100 and 0 <= self.english <= 100):
                    raise User_Exception("점수는 0에서 100사이의 수입니다", 2)
            except ValueError:
                raise User_Exception("점수는 숫자여야 합니다", 2)
        except User_Exception as e:
            return print(e)

    def process_sungjuk(self):
        self.sum_score = self.korean + self.math + self.english
        self.avg = self.sum_score / 3

        if self.avg >= 90:
            self.grade = "수"
        elif self.avg >= 80:
            self.grade = "우"
        elif self.avg >= 70:
            self.grade = "미"
        elif self.avg >= 60:
            self.grade = "양"
        else:
            self.grade = "가"




    @classmethod
    def input_data(cls):
        try:
            student = Sungjuk()
            student.input_sungjuk()
            connection = Db_Connection()

            student.process_sungjuk()
            print(student)
            connection.dbconnection("INSERT", student.hakbun, student.name, student.korean, student.math, student.english, student.avg, student.sum_score, student.grade, hakbun= student.hakbun)
        except User_Exception as e:
            print(e)

    @classmethod
    def output_data(cls):
        connection = Db_Connection()
        selectByAll = connection.dbconnection("SELECT", )
        print("\n                      *** 성적표 ***")
        print("============================================================")
        print("학번    이름    국어    영어    수학    총점    평균     등급")
        for i in selectByAll:
            print(i)
        print("============================================================")
        print(f"\t\t 총학생수 = {0},  전체 평균 = { 0:.2f}\n")



    def search_data(self):
        hakbun = input("\n조회할 학번을 입력하세요: ")
        # student = Sungjuk()
        # student.set_hakbun(hakbun)
        connection = Db_Connection()
        selectByOne = connection.dbconnection("SELECTBYONE",hakbun, hakbun =hakbun)
        print("============================================================")
        print("학번    이름    국어    영어    수학    총점    평균     등급")
        print("============================================================")
        print(selectByOne)

    def modify_data(self):
            hakbun = input("\n수정할 학번을 입력하세요: ")
            student = Sungjuk()
            student.set_hakbun(hakbun)
            student.input_sungjuk("modify")
            connection = Db_Connection()

            student.process_sungjuk()
            print(student)
            connection.dbconnection("UPDATE",  student.name, student.korean, student.math,
                                    student.english, student.avg, student.sum_score, student.grade,student.hakbun,
                                    hakbun= hakbun)

    def delete_data(self):
        hakbun = input("\n삭제할 학번을 입력하세요: ")
        student = Sungjuk()
        student.set_hakbun(hakbun)
        connection = Db_Connection()
        student.process_sungjuk()
        print(student)
        connection.dbconnection("DELETE",student.hakbun,
                                hakbun=hakbun)
