def test():
    print("test() 의 첫줄입니다")
    try:
        print("try구문이 실행되었습니다")
        return   #실행순서를 잘봐야함 return이 있고 없고를 봐야함
        print("try구문이 return 키워드 뒤입니다")
    except:
        print("except구문이 실행되었습니다")
    else:
        print("else구문이 실행되었습니다")
    finally:
        print("finally구문이 실행되었습니다")
    print("test() 함수의 마지막 줄입니다")

test()