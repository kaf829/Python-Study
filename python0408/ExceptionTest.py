class User_Exception(Exception):
    def __init__(self, msg1, msg2='', flag=0):
        self._message1 = msg1
        self._message2 = msg2
        self.flag = flag

    def __str__(self):
        if self.flag == 1:
            return f"숫자 에러: {self._message1} {self._message2}"
        elif self.flag == 2:
            return f"인덱스 에러: {self._message1} {self._message2}"
        else:
            return f"{self._message1} {self._message2}"

def input_proc(s_lst):
    try:
        data = {}
        data["item_no"] = input("제품번호를 입력하세요 : ")
        for obj in s_lst:
            if obj["item_no"] == data["item_no"]:
                raise User_Exception("기존에 존재하는 제품번호입니다", flag=2)

        data["item_name"] = input("이름을 입력하세요 : ")
        data["count"] = int(input("수량 => : "))
        data["price"] = int(input("가격 => : "))
        data["total_price"] = data["count"] * data["price"]

        s_lst.append(data)
        print("\n품목정보 입력 성공!!\n")
    except User_Exception as e:
        print(e)

def search_proc(s_lst):
    try:
        item_no = input("\n조회할 제품번호를 입력하세요 : ")
        for data in s_lst:
            if data["item_no"] == item_no:
                print("\n제품번호    제품명    수량    단가    금액    ")
                print("============================================================")
                print("%4s  %4s   %3d     %3d     %3d"
                      % (data["item_no"], data["item_name"], data["count"], data["price"],
                         data["total_price"]))
                print("============================================================\n")
                break
        else:
            raise User_Exception(f"제품번호 {item_no}은 존재하지 않습니다", flag=2)
    except User_Exception as e:
        print(e)

def input_score(msg):
    try:
        num = int(input(f"{msg}를 입력하세요: "))
        if num < 0 or num > 100:
            raise User_Exception(f"{msg}는 0 이상으로 숫자를 입력해주세요", flag=1)
    except ValueError:
        print("숫자를 입력해주세요")
        return input_score(msg)
    except User_Exception as e:
        print(e)
        return input_score(msg)
    else:
        return num

def input_menu():
    try:
        menu = int(input("\n메뉴를 선택하세요 : "))
        if menu < 1 or menu > 6:
            raise User_Exception("메뉴는 1에서 6 사이의 숫자여야 합니다", f"입력한 메뉴: {menu}", flag=1)
        else:
            return menu
    except ValueError:
        print("숫자를 입력해주세요")
        return
    except User_Exception as e:
        print(e)

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


if __name__ == "__main__":
    lst = []
    while True:
        menu = input_menu()
        if menu == 1:
            input_proc(lst)
        elif menu == 2:
            output_proc(lst)
        elif menu == 3:
            search_proc(lst)
        elif menu == 6:
            print("\n프로그램 종료...")
            break
        else:
            print("\n메뉴를 다시 입력하세요!!!\n")