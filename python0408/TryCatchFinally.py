try:
    number_input_a = int(input("정수입력"))
    print("원의 반지름:", number_input_a)   #=> 이렇게 작성해도 되지만 ELSE문으로 분리하여 작성할 수 있음
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", number_input_a * number_input_a)
except:
    print("정수를 입력하지 않았습니다")
else:
    print("예외가 발생하지 않습니다")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다")
