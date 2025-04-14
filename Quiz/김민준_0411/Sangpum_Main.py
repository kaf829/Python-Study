from Sangpum_service import Sangpum_service

def title_menu():
    print(" *** 메뉴 ***")
    print("1. 상품정보 입력")
    print("2. 상품정보 출력")
    print("3. 상품정보 조회")
    print("4. 상품정보 수정")
    print("5. 상품정보 삭제")
    print("6. 프로그램 종료")

if __name__ == "__main__":
    while True:
        title_menu()
        menu = int(input("\n메뉴를 선택하세요: "))
        sangpum = Sangpum_service()
        if menu == 1:
            sangpum.input_data()
        elif menu == 2:
            sangpum.output_data()
        elif menu == 3:
            sangpum.search_data()
        elif menu == 4:
            sangpum.modify_data()
        elif menu == 5:
            sangpum.delete_data()
        elif menu == 6:
            print("\n프로그램 종료...")
            break
        else:
            print("\n메뉴를 다시 입력하세요!!!\n")
