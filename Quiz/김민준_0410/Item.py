from python0410.User_Exception import User_Exception


class Item:
    lst = []

    def __init__(self):
        self.item_no = ""
        self.item_name = ""
        self.price = 0
        self.count = 0
        self.sum_price = 0

    # key값은 수정할시 hakbun재입력이 필요없기 떄문에 작성(기본값: 전체 input , key = "?" : 학번 입력X )
    def input_item(self, key =""):
        try:
            if not key:
                self.item_no = input("품번을 입력하세요: ")

            self.item_name = input("품명을 입력하세요: ")
            try:
                self.price = int(input("가격을 입력하세요: "))
                self.count = int(input("상품 갯수를 입력하세요: "))
                if not (0 <= self.price or 0 <= self.count  ):
                    raise User_Exception("가격과 갯수는 0 이상입니다",2)
            except ValueError:
                raise User_Exception("가격과 갯수는 숫자여야 합니다",2)
        except User_Exception as e:
            print(e)

    def process_price(self):
        self.sum_price = self.price * self.count

    # key값으로 인해 전체 데이터를 출력하는지 한개의 데이터를 출력하는지 기준이 됨 (기본값: 전체, "ONE" : 1개)
    def output_item(self ,key = ""):
        if key:
            print("============================================================")
            print("제품코드     제품명    가격    수량    단가    판매금액")
            print("============================================================")
        print(f"{self.item_no}      {self.item_name}        {self.price}        {self.count}        {self.sum_price}")

    @classmethod
    def input_data(cls):
        try:
            item = Item()
            item.input_item()
            for obj in cls.lst:
                if obj.item_no == item.item_no:
                    raise User_Exception(f"{item.item_no}", 3)
            item.process_price()
            cls.lst.append(item)
        except User_Exception as e:
            print(e)

    @classmethod
    def output_data(cls):
        try:
            if cls.lst:
                total_sum = 0
                print("\n                      *** 성적표 ***")
                print("============================================================")
                print("제품코드    제품명    수량    단가    판매금액    ")
                print("============================================================")
                for item in cls.lst:
                    item.output_item()
                    total_sum += item.sum_price
                print(f"\t\t 총 상품 수 = {len(cls.lst)},  전체 가격 = {total_sum :.2f}\n")
            else:
                raise User_Exception("리스트 안", 1)
        except User_Exception as e:
            print(e)

    @classmethod
    def search_data(cls):
        try:
            item_no = input("\n조회할 품번을 입력하세요: ")
            for item in cls.lst:
                if item.item_no == item_no:
                    item.output_item("one")
                    break
            else:
                raise User_Exception(f'{item_no}', 1)
        except User_Exception as e:
            print(e)

    @classmethod
    def modify_data(cls):
        try:
            item_no = input("\n수정할 품번을 입력하세요: ")
            for item in cls.lst:
                if item.item_no == item_no:
                    item.input_item('modify')
                    item.process_price()
                    print(f"\n품번 {item.item_no} 성적정보 수정 성공!\n")
                    break
            else:
                raise User_Exception(f"{item_no}", 1)
        except User_Exception as e:
            print(e)

    @classmethod
    def delete_data(cls):
        try:
            item_no = input("\n삭제할 품번을 입력하세요: ")
            for item in cls.lst:
                if item.item_no == item_no:
                    cls.lst.remove(item)
                    print(f"품번 {item_no} 품번정보 삭제 성공!!\n")
                    break
            else:
                raise User_Exception(f"{item_no}", 1)
        except User_Exception as e:
            print(e)
