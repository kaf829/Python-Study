class User_Exception(Exception):
    def __init__(self, msg1, msg2= ''):
        self._message1 = msg1
        self._message2 = msg2


def title_menu():
    print(" *** 메뉴 ***")
    print("1. 제품정보 입력")
    print("2. 제품정보 출력")
    print("3. 제품정보 조회")
    print("4. 제품정보 수정")
    print("5. 제품정보 삭제")
    print("6. 프로그램 종료")


def input_proc(s_lst):
    try:

        data = {}

        data["item_no"] = input("제품번호를 입력하세요 : ")
        for obj in s_lst:
            if obj["item_no"] == data["item_no"]:
                raise User_Exception("기존에 존재하는 학번입니다")

        data["item_name"] = input("이름을 입력하세요 : ")
        data["count"] = int(input("수량 => : "))
        data["price"] = int(input("가격 => : "))
        data["total_price"] = data["count"]*data["price"]

        s_lst.append(data)
        print("\n품목정보 입력 성공!!\n")
    except User_Exception as e:
        print(e.args)



def output_proc(s_lst):
    try:
        if s_lst:
            print("\n             *** 성적표 ***")
            print("============================================")
            print("제품번호    제품이름    수량    단가    금액    ")
            print("============================================")
            total_price_all = 0
            for data in s_lst:
                total_price_all += data["total_price"]
                print("%4s  %8s   %8d     %4d     %3d"
                      % (data["item_no"], data["item_name"], data["count"], data["price"],
                         data["total_price"]))

            print("==============================================")

            print("총 금액",  total_price_all)
        else:
            raise User_Exception("등록된 정보가 없습니다")
    except User_Exception as e:
        print(e.args)

def search_proc(s_lst):
    try:

        item_no = input("\n조회할 품번을 입력하세요 : ")
        for data in s_lst:
            if (data["item_no"] == item_no):
                print("\n제품번호    제품명    수량    단가    금액    ")
                print("============================================================")
                print("%4s  %4s   %3d     %3d     %3d"
                      % (data["item_no"], data["item_name"], data["count"], data["price"],
                         data["total_price"]))
                print("============================================================\n")
                break
        else:
            raise User_Exception(f"품번 {item_no}은 존재하지 않습니다")
    except User_Exception as e:
        print(e.args)


def update_proc(s_lst):
    try:
        item_no = input("\n수정할 품번을 입력하세요 : ")
        for data in s_lst:
            if (data["item_no"] == item_no):
                data["item_name"] = input("이름을 입력하세요 : ")
                data["count"] = input_score("수량")
                data["price"] = input_score("가격")
                data["total_price"] = data["count"] * data["price"]


                print("\n품번 %s 성적정보 수정 성공!\n" % data["item_no"])
                break
        else:
            raise User_Exception(f"품번 {item_no}가 존재하지 않습니다")

    except User_Exception as e:
        print(e.args)


def delete_proc(s_lst):
    try:
        item_no = input("\n삭제할 품번을 입력하세요 : ")
        for data in s_lst:
            if (data["item_no"] == item_no):
                s_lst.remove(data)
                print("\n품번 %s 품목정보 삭제 성공!!\n" % data["item_no"])
                break
        else:
            raise User_Exception(f"품번 {item_no}가 존재하지 않습니다")
    except User_Exception as e:
        print(e.args)

def input_score(msg):
    try:
        num = int(input(f"{msg}를 입력하세요"))
        if num < 0 or num > 100:
            raise User_Exception(f"{msg}는 0 이상으로 숫자를 입력해주세요")
    except ValueError:
        print("숫자를 입력해주세요")
        return input_score(msg)
    except User_Exception as e:
        print(e.args)
        return input_score(msg)
    else:
        return num

def input_menu():
    try:
        menu = int(input("\n메뉴를 선택하세요 : "))
        if menu < 1 or menu > 6:
            raise User_Exception("메뉴는 1에서 6 사이의 숫자여야 합니다", f"입력한 Menu: {menu}")
        else:
            return menu
    except ValueError:
        print("숫자를 입력해주세요")
        return
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