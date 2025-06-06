from Sungjeok_DB.Score_Test import Sungjuk

def title_menu():
    print(" *** 메뉴 ***")
    print("1. 성적정보 입력")
    print("2. 성적정보 출력")
    print("3. 성적정보 조회")
    print("4. 성적정보 수정")
    print("5. 성적정보 삭제")
    print("6. 프로그램 종료")

if __name__ == "__main__":
    while True:
        title_menu()
        menu = int(input("\n메뉴를 선택하세요: "))
        sungjuk = Sungjuk()
        if menu == 1:
            sungjuk.input_data()
        elif menu == 2:
            sungjuk.output_data()
        elif menu == 3:
            sungjuk.search_data()
        elif menu == 4:
            sungjuk.modify_data()
        elif menu == 5:
            sungjuk.delete_data()
        elif menu == 6:
            print("\n프로그램 종료...")
            break
        else:
            print("\n메뉴를 다시 입력하세요!!!\n")
