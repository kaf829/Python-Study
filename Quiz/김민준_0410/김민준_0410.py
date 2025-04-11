
class Sangpum:
    def __init__(self):
        self.item_no =""
        self.item_name=""
        self.price = 0
        self.count = 0
        self.total_pirce = 0

    def input_data(self):
        self.itme_no = input("상품코드를 입력하세요 : ")
        self.item_name = input("상품명을 입력하세요 : ")
        self.count = int(input("수량을 입력하세요 : "))
        self.price = int(input("단가를 입력하세요 : "))
        print()

    def proc_data(self):
        self.total_pirce = self.count * self.price

    def output_data(self):
        print("\t\t\t ***제품 정보***")
        print("=" * 50)
        print("제품 코드     제품명    수량     단가     금액")
        print("=" * 50)
        print(f'{self.itme_no}, {self.item_name}, {self.count}, {self.price}, {self.total_pirce}')
        print("=" * 50)



sangpum = Sangpum()
sangpum.input_data()
sangpum.proc_data()
sangpum.output_data()