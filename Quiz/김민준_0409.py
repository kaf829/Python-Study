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


    def input_sungjuk(self):
        self.hakbun  = input(f"학번을 입력하세요")
        self.name = input(f"이름을 입력하세요")
        self.korean = int(input(f"국어 점수를 입력하세요"))
        self.math = int(input(f"수학 점수를 입력하세요"))
        self.english = int(input(f"영어 점수를 입력하세요"))



    def prcess_sungjeok(self):
        self.sum_score = self.korean + self.math + self.english
        self.avg = self.sum_score / 3


        if self.avg > 90:
            self.grade = "수"
        elif self.avg > 80:
            self.grade = "우"
        elif self.avg > 70:
            self.grade = "미"
        elif self.avg > 60:
            self.grade = "양"
        elif self.avg > 70:
            self.grade = "가"



    def output_sungjeok(self):
        print("=======================================================")
        print("학번 \t 이름 \t 국어 \t 영어 \t 수학 \t 총점 \t 평균 \t 등급")
        print(f"{self.hakbun} \t {self.name} \t {self.korean} \t {self.english} \t {self.math} \t {self.sum_score} \t {self.avg} \t {self.grade}")




student = Sungjuk()
student.input_sungjuk()
student.prcess_sungjeok()
student.output_sungjeok()



