class User_Exception(Exception):
    def __init__(self, msg1, msg2= ''):
        self._message1 = msg1
        self._message2 = msg2


def title_menu():
    print(" *** 메뉴 ***")
    print("1. 성적정보 입력")
    print("2. 성적정보 출력")
    print("3. 성적정보 조회")
    print("4. 성적정보 수정")
    print("5. 성적정보 삭제")
    print("6. 프로그램 종료")


def input_proc(s_lst):
    try:
        data = {}

        data["hakbun"] = input("\n학번을 입력하세요 : ")
        for obj in s_lst:
            if obj["hakbun"] == data["hakbun"]:
                raise User_Exception("기존에 존재하는 학번입니다")


        data["irum"] = input("이름을 입력하세요 : ")
        data["kor"] = input_score("국어")
        data["eng"] = input_score("영어")
        data["math"] = input_score("수학")
        print( data["kor"])
        print( data["eng"])
        print( data["math"])
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
        print("\n성적정보 입력 성공!!\n")

    except User_Exception as e:
        print(e.args)
        return input_proc(s_lst)


def output_proc(s_lst):
    try:
        if s_lst:
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
        else:
            raise User_Exception("등록된 정보가 없습니다")
    except User_Exception as e:
        print(e.args)


def search_proc(s_lst):
    try:
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
            raise User_Exception(f"학번 {hakbun}은 존재하지 않습니다")
    except User_Exception as e:
        print(e.args)


def update_proc(s_lst):
    try:
        hakbun = input("\n수정할 학번을 입력하세요 : ")
        for data in s_lst:
            if (data["hakbun"] == hakbun):
                data["kor"] = input_score("국어")
                data["eng"] = input_score("영어")
                data["math"] = input_score("수학")
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
            raise User_Exception(f"학번 {hakbun}은 존재하지 않습니다")
    except User_Exception as e:
        print(e.args)


def delete_proc(s_lst):
    try:
        hakbun = input("\n삭제할 학번을 입력하세요 : ")
        for data in s_lst:
            if (data["hakbun"] == hakbun):
                s_lst.remove(data)
                print("\n학번 %s 성적정보 삭제 성공!!\n" % data["hakbun"])
                break
        else:
            raise User_Exception(f"학번 {hakbun}은 존재하지 않습니다")
    except User_Exception as e:
        print(e.args)


def input_score(subject):
    try:
        score = int(input(f"{subject} 점수를입력하세요"))
        if score < 0 or score > 100:
            raise User_Exception(f"{subject}점수는 0 ~ 100 사이의 숫자여야 합니다")
    except ValueError:
        print("숫자를 입력해주세요")
        return input_score(subject)
    except User_Exception as e:
        print(e.args)
        return input_score(subject)
    else:
        return score



def input_menu():
    try:
        menu = int(input("\n메뉴를 선택하세요 : "))
        if menu < 1 or menu > 6:
            raise User_Exception("메뉴는 1에서 6 사이의 숫자여야 합니다", f"입력한 Menu: {menu}")
        else:
            return menu
    except User_Exception as e:
            print(e.args)


if __name__ == "__main__":
    lst = []
    while True:
        title_menu()
        menu = input_menu()
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

