print("프로그램이 시작되었습니다")

while True:
    try:
        print("try구문이 실행되었습니다")
        print(3/0)
        print("try구문의 break 키워드 뒤입니다")
    except ZeroDivisionError as e:
        print("except구문이 실행되었습니다", e.args[0])
    finally:
        print("finally구문이 실행되었습니다")
    print("while 반복문의 마지막 줄입니다")

print("프로그램이 종료되었습니다")
