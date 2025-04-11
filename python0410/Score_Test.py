from python0410.User_Exception import User_Exception


class Sungjuk:
    lst = []

    def __init__(self):
        self.hakbun = ""
        self.name = ""
        self.korean = 0
        self.math = 0
        self.english = 0
        self.sum_score = 0
        self.avg = 0
        self.grade = ""

    # key값은 수정할시 hakbun재입력이 필요없기 떄문에 작성(기본값: 전체 input , key = "?" : 학번 입력X )
    def input_sungjuk(self, key =""):
        try:
            if not key:
                self.hakbun = input("학번을 입력하세요: ")

            self.name = input("이름을 입력하세요: ")
            try:
                self.korean = int(input("국어 점수를 입력하세요: "))
                self.math = int(input("수학 점수를 입력하세요: "))
                self.english = int(input("영어 점수를 입력하세요: "))
                if not (0 <= self.korean <= 100 or 0 <= self.math <= 100 or 0 <= self.engilsh <= 100):
                    raise User_Exception("점수는 0에서 100사이의 수입니다",2)
            except ValueError:
                raise User_Exception("점수는 숫자여야 합니다",2)
        except User_Exception as e:
            print(e)

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

    # key값으로 인해 전체 데이터를 출력하는지 한개의 데이터를 출력하는지 기준이 됨 (기본값: 전체, "ONE" : 1개)
    def output_sungjuk(self ,key = ""):
        if key:
            print("============================================================")
            print("학번    이름    국어    영어    수학    총점    평균     등급")
            print("============================================================")
        print(f"{self.hakbun}    {self.name}    {self.korean}    {self.english}    {self.math}    {self.sum_score}    {self.avg:.2f}    {self.grade}")

    @classmethod
    def input_data(cls):
        try:
            student = Sungjuk()
            student.input_sungjuk()
            for obj in cls.lst:
                if obj.hakbun == student.hakbun:
                    raise User_Exception(f"{student.hakbun}", 3)
            student.process_sungjuk()
            cls.lst.append(student)
        except User_Exception as e:
            print(e)

    @classmethod
    def output_data(cls):
        try:
            if cls.lst:
                total_avg = 0
                for student in cls.lst:
                    student.output_sungjuk()
                    total_avg += student.avg
                print("\n                      *** 성적표 ***")
                print("============================================================")
                print("학번    이름    국어    영어    수학    총점    평균     등급")
                print("============================================================")
                print(f"\t\t 총학생수 = {len(cls.lst)},  전체 평균 = {total_avg / len(cls.lst):.2f}\n")
            else:
                raise User_Exception("리스트 안", 1)
        except User_Exception as e:
            print(e)

    @classmethod
    def search_data(cls):
        try:
            hakbun = input("\n조회할 학번을 입력하세요: ")
            for student in cls.lst:
                if student.hakbun == hakbun:
                    student.output_sungjuk("one")
                    break
            else:
                raise User_Exception(f'{hakbun}', 1)
        except User_Exception as e:
            print(e)

    @classmethod
    def modify_data(cls):
        try:
            hakbun = input("\n수정할 학번을 입력하세요: ")
            for student in cls.lst:
                if student.hakbun == hakbun:
                    student.input_sungjuk('modify')
                    student.process_sungjuk()
                    print(f"\n학번 {student.hakbun} 성적정보 수정 성공!\n")
                    break
            else:
                raise User_Exception(f"{hakbun}", 1)
        except User_Exception as e:
            print(e)

    @classmethod
    def delete_data(cls):
        try:
            hakbun = input("\n삭제할 학번을 입력하세요: ")
            for student in cls.lst:
                if student.hakbun == hakbun:
                    cls.lst.remove(student)
                    print(f"\n학번 {hakbun} 성적정보 삭제 성공!!\n")
                    break
            else:
                raise User_Exception(f"{hakbun}", 1)
        except User_Exception as e:
            print(e)
