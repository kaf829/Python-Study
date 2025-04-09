class MenuException(Exception):
    def __init__(self, msg):
        self._msg = msg

class JumsuException(Exception):
    def __init__(self, msg):
        self._msg = msg

def input_jumsu(msg):
    while True:
        try:
            jumsu = int(input(msg))
            if 0 > jumsu or jumsu > 100:
                raise JumsuException("점수는 0~100사이만 입력능합니다!!!")
            return jumsu
        except ValueError:
            print("\n점수 입력 오류 => 숫자만 입력가능합니다!!!\n")
        except JumsuException as e:
            print("\n점수 입력 오류 => %s\n" % e)

def title_menu():
    print(" *** 메뉴 ***")
    print("1. 성적정보 입력")
    print("2. 성적정보 출력")
    print("3. 성적정보 조회")
    print("4. 성적정보 수정")
    print("5. 성적정보 삭제")
    print("6. 프로그램 종료")


def input_proc(s_lst):
    data = {}

    data["hakbun"] = input("\n학번을 입력하세요 : ")
    for obj in s_lst:
        if obj["hakbun"] == data["hakbun"]:
            print("\n학번 중복 오류!!!\n")
            return
    data["irum"] = input("이름을 입력하세요 : ")
    data["kor"] = input_jumsu("국어점수를 입력하세요 : ")
    data["eng"] = input_jumsu("영어점수를 입력하세요 : ")
    data["math"] = input_jumsu("수학점수를 입력하세요 : ")
    data["tot"] = data["kor"] + data["eng"] + data["math"]
    data["avg"] = data["tot"] / 3
    if data["avg"] >= 90:
        data["grade"] = "수"
    elif data["avg"] >= 80:
        data["grade"] = "우"
    elif data["avg"] >= 70:
        data["grade"] = "미"
    elif data["avg"] >= 60:
        data["grade"] = "양"
    else:
        data["grade"] = "가"

    s_lst.append(data)
    print("\n성적정보 입력 성공!!\n");


def output_proc(s_lst):
    if len(s_lst) == 0:
        print("\n출력할 데이터가 없습니다.\n")
        return

    print("\n                      *** 성적표 ***")
    print("============================================================")
    print("학번    이름    국어    영어    수학    총점    평균     등급")
    print("============================================================")
    total_avg = 0
    for data in s_lst:
        total_avg += data["avg"]
        print("%4s  %4s   %3d     %3d     %3d     %3d   %6.2f     %s"
              % (data["hakbun"], data["irum"], data["kor"], data["eng"],
                 data["math"], data["tot"], data["avg"], data["grade"]))

    print("============================================================")
    print("\t\t 총학생수 = %d,  전체 평균 = %.2f\n"
          % (len(s_lst), total_avg / len(s_lst)))


def search_proc(s_lst):
    hakbun = input("\n조회할 학번을 입력하세요 : ")
    for data in s_lst:
        if (data["hakbun"] == hakbun):
            print("\n학번    이름    국어    영어    수학    총점    평균     등급")
            print("============================================================")
            print("%4s  %4s   %3d     %3d     %3d     %3d   %6.2f     %s"
                  % (data["hakbun"], data["irum"], data["kor"], data["eng"],
                     data["math"], data["tot"], data["avg"], data["grade"]))
            print("============================================================\n")
            break
    else:
        print("\n조회할 학번 %s가 없습니다!!\n" % hakbun)


def update_proc(s_lst):
    hakbun = input("\n수정할 학번을 입력하세요 : ")
    for data in s_lst:
        if (data["hakbun"] == hakbun):
            data["kor"] = input_jumsu("국어점수를 입력하세요 : ")
            data["eng"] = input_jumsu("영어점수를 입력하세요 : ")
            data["math"] = input_jumsu("수학점수를 입력하세요 : ")
            data["tot"] = data["kor"] + data["eng"] + data["math"]
            data["avg"] = data["tot"] / 3.
            if data["avg"] >= 90:
                data["grade"] = "수"
            elif data["avg"] >= 80:
                data["grade"] = "우"
            elif data["avg"] >= 70:
                data["grade"] = "미"
            elif data["avg"] >= 60:
                data["grade"] = "양"
            else:
                data["grade"] = "가"
            print("\n학번 %s 성적정보 수정 성공!\n" % data["hakbun"])
            break
    else:
        print("\n수정할 학번 %s가 없습니다!!\n" % hakbun)


def delete_proc(s_lst):
    hakbun = input("\n삭제할 학번을 입력하세요 : ")
    for data in s_lst:
        if (data["hakbun"] == hakbun):
            s_lst.remove(data)
            print("\n학번 %s 성적정보 삭제 성공!!\n" % data["hakbun"])
            break
    else:
        print("\n삭제할 학번 %s가 없습니다!!\n" % hakbun)


if __name__ == "__main__":
    lst = []
    while True:
        title_menu()
        try:
            menu = int(input("\n메뉴를 선택하세요 : "))
            if menu < 1 or menu > 6:
                raise MenuException("숫자1~6를 입력하세요!!!")
        except ValueError:
            print("\n메뉴 입력 오류 => 숫자만 입력가능합니다!!!\n")
            continue
        except MenuException as e:
            print("\n메뉴 입력 오류 => %s\n" % e)
            continue

        if menu == 1:
            input_proc(lst)
        elif menu == 2:
            output_proc(lst)
        elif menu == 3:
            search_proc(lst)
        elif menu == 4:
            update_proc(lst)
        elif menu == 5:
            delete_proc(lst)
        elif menu == 6:
            print("\n프로그램 종료...")
            break
        else:
            print("\n메뉴를 다시 입력하세요!!!\n")