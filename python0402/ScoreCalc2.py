
from tabulate import tabulate

data_list = [input("학번 입력 => "),
input("이름 입력 => "),
int(input("국어 입력 =>")),
int(input("영어 입력 =>")),
int(input("수학 입력 =>"))
             ]

data_list.append(data_list[2]+data_list[3]+data_list[4])
data_list.append(data_list[5]/3)
grade = ""
while True:
    if data_list[6] > 90:
        grade ="수"
        break
    if data_list[6] > 80:
        grade = "우"
        break
    if data_list[6] > 70:
        grade = "미"
        break
    if data_list[6] > 60:
        grade = "양"
        break
    if data_list[6] > 50:
        grade = "가"
        break

data_list.append(grade)

data = [[
    i for i in data_list
]]


print("\t\t\t\t\t\t\t ***성적표***")
print("-"*50)
# print("=" * 50)
print(tabulate(data, headers=["학번", "이름", "국어", "영어", "수학", "총점", "평균", "등급"], stralign="center", tablefmt="plain"))
# print("=" * 50)


# print("%4s %3s %4d  %4d  %4d    %4d     %5.2f" % (hakbun, irum, int(kor), int(eng), int(math), tot, avg))
