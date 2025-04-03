
from tabulate import tabulate

data_list = {"hakbun":input("학번 입력 => "),
"irum": input("이름 입력 => "),
"kor": int(input("국어 입력 =>")),
"eng": int(input("영어 입력 =>")),
"math" : int(input("수학 입력 =>"))
             }



data_list["sum"] = data_list["kor"] + data_list["eng"] + data_list["math"]
data_list['avg'] = data_list['sum'] / 3
grade = ""
while True:
    if data_list['avg'] > 90:
        grade ="수"
        break
    if data_list['avg'] > 80:
        grade = "우"
        break
    if data_list['avg'] > 70:
        grade = "미"
        break
    if data_list['avg'] > 60:
        grade = "양"
        break
    if data_list['avg'] > 50:
        grade = "가"
        break

data_list['grade'] = grade

data = [[
    value for value in data_list.values()
]]


print("\t\t\t\t\t\t\t ***성적표***")
print("-"*50)
# print("=" * 50)
print(tabulate(data, headers=["학번", "이름", "국어", "영어", "수학", "총점", "평균", "등급"], stralign="center", tablefmt="plain"))
# print("=" * 50)


# print("%4s %3s %4d  %4d  %4d    %4d     %5.2f" % (hakbun, irum, int(kor), int(eng), int(math), tot, avg))
