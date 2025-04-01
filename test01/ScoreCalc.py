
from tabulate import tabulate

hakbun = input("학번 입력 => ")
irum  = input("이름 입력 => ")
kor = input("국어 입력 =>")
eng = input("영어 입력 =>")
math = input("수학 입력 =>")

tot = int(kor) + int(eng) + int(math)
avg = tot/3
grade = ""
while True:
    if avg > 90:
        grade ="수"
        break
    if avg > 80:
        grade = "우"
        break
    if avg > 70:
        grade = "미"
        break
    if avg > 60:
        grade = "양"
        break
    if avg > 50:
        grade = "가"
        break


data = [[
    hakbun,
    irum,
    str(kor),
    str(eng),
    str(math),
    str(tot),
    f"{avg:.2f}",
    grade
]]


print("\t\t\t\t\t\t\t ***성적표***")
print("-"*50)
# print("=" * 50)
print(tabulate(data, headers=["학번", "이름", "국어", "영어", "수학", "총점", "평균", "등급"], stralign="center", tablefmt="plain"))
# print("=" * 50)


# print("%4s %3s %4d  %4d  %4d    %4d     %5.2f" % (hakbun, irum, int(kor), int(eng), int(math), tot, avg))
