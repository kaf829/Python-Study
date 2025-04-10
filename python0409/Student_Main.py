from python0409.Student import Student

students = [
    Student("윤인성",87,98,88,95),
    Student("연하진",92,98,96,98),
    Student("나선주",98,92,98,98),
    Student("윤아린",95,98,98,98),
    Student("윤명월",64,88,92,92)
    ]




print("이름",     "총점",    "평균",sep='\t')
for student in students:
    print(Student.to_string(student))

print(Student.count)
Student.print()