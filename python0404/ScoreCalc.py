
from tabulate import tabulate


def input_data():
    while True:
        data_list = {}
        hakbun = input("학번입력").upper()
        if hakbun == "EXIT":
            return
        data_list["학번"] = hakbun
        data_list["irum"] = input("이름입력 => ")
        data_list["kor"] = int(input("국어입력 => "))
        data_list["eng"] = int(input("영어입력 => "))
        data_list["math"] = int(input("수학입력 => "))
        data_list["sum"] = data_list["kor"] + data_list["eng"] + data_list["math"]
        data_list['avg'] = data_list['sum'] / 3
        grade = ""
        while True:
            if data_list['avg'] > 90:
                grade = "수"
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
        result.append(data_list)



def print_data(result):
    data = []
    tot_sum = 0
    for i in range(len(result)):
        value = [value for value in result[i].values()]
        data.append(value)

    print("\t\t\t\t\t\t\t ***성적표***")
    print("-"*50)
    # print("=" * 50)
    print(tabulate(data, headers=["학번", "이름", "국어", "영어", "수학", "총점", "평균", "등급"], stralign="center", tablefmt="plain"))
    # print("=" * 50)

    print("학생수:", len(result))
    for i in range(len(data)):
        tot_sum += int(data[i][5])
    print("총평균", tot_sum /len(result))



result = []
input_data()
print_data(result)

