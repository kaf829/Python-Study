
from tabulate import tabulate

def menu_title():
    print("        ** 메뉴 **        ")
    print("1. 성적 입력")
    print("2. 성적 출력")
    print("3. 성적 조회")
    print("4. 성적 수정")
    print("5. 성적 삭제")
    print("6. 프로그램 종료")


def input_data():

    data_list = {}
    hakbun = input("학번입력").upper()
    if result:
        for data in result:
            if data["학번"] == hakbun:
                return print("중복된 학번이 있습니다")


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

    print("입력성공!!")

def modify_score():
    modify_hakbun = input("수정할 학번입력 =>")
    if result:
        for i in range(len(result)):
            if result[i]["학번"] == modify_hakbun:
                result[i]["irum"] = input("이름입력 => ")
                result[i]["kor"] = int(input("국어입력 => "))
                result[i]["eng"] = int(input("영어입력 => "))
                result[i]["math"] = int(input("수학입력 => "))
                result[i]["sum"] = result[i]["kor"] + result[i]["eng"] + result[i]["math"]
                result[i]['avg'] = result[i]['sum'] / 3

                grade = ""
                if result[i]['avg'] > 90:
                    grade = "수"

                if result[i]['avg'] > 80:
                    grade = "우"

                if result[i]['avg'] > 70:
                    grade = "미"

                if result[i]['avg'] > 60:
                    grade = "양"

                if result[i]['avg'] > 50:
                    grade = "가"

                result[i]['grade'] = grade
                return print("수정 성공")
            if result[i]["학번"] != modify_hakbun:
                print("학번을 잘못입력하였습니다")
                return


def info_student():
    search_hakbun = input("조회할 학번입력 =>")
    if result:
        for i in range(len(result)):
            if result[i]["학번"] == search_hakbun:
                print_data([result[i]["학번"]])
                return
            else:
                return print("조회할 학번이 틀렸습니다")

def remove_score():
    search_hakbun = input("조회할 학번입력 =>")
    if result:
        for i in range(len(result)):
            if result[i]["학번"] == search_hakbun:
                result.remove(result[i])
                return print(f"{search_hakbun}을 삭제하였습니다")
            else:
                return print("삭제할 학번이 틀렸습니다")





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


if __name__ == "__main__":
    result = []
    while True:
        menu_title()
        menu = int(input("\n메뉴 선택 =>"))

        if menu == 1:
            input_data()
        elif menu == 2:
            if not result:
                print("입력된 정보가 없습니다")
            print_data(result)
        elif menu == 3:
            if not result:
                print("입력된 정보가 없습니다")
            info_student()
        elif menu == 4:
            if not result:
                print("입력된 정보가 없습니다")
            modify_score()
        elif menu == 5:
            if not result:
                print("입력된 정보가 없습니다")
            remove_score()

        elif menu == 6:
            print("\n프로그램을 종료합니다")
            break
        else:
            print("메뉴를 다시 선택하세욘")

