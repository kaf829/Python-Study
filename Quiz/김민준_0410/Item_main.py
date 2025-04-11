from Quiz.김민준_0410.Item import Item


def title_menu():
    print(" *** 메뉴 ***")
    print("1. 품목 입력")
    print("2. 품목정보 출력")
    print("3. 품목정보 조회")
    print("4. 품목정보 수정")
    print("5. 품목정보 삭제")
    print("6. 프로그램 종료")

if __name__ == "__main__":
    while True:
        title_menu()
        menu = int(input("\n메뉴를 선택하세요: "))
        if menu == 1:
            Item.input_data()
        elif menu == 2:
            Item.output_data()
        elif menu == 3:
            Item.search_data()
        elif menu == 4:
            Item.modify_data()
        elif menu == 5:
            Item.delete_data()
        elif menu == 6:
            print("\n프로그램 종료...")
            break
        else:
            print("\n메뉴를 다시 입력하세요!!!\n")
