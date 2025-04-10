class Student:
    students = []
    count = 0

    @classmethod
    def print(cls):
        print("----- 학생목록 ------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))

    def __init__(self,name,korean,math,english,science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count +=1
        Student.students.append(self)

    def __str__(self):
        return " {} \t {}\t {}".format(self.name,self.get_sum(),self.get_average())


    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_average())

    #def __del__(self):
      # print(f"{Student.count}번째 학생이 제거되었습니다")
     #  Student.count -=1

