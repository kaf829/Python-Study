
try:
    number_input_a = int(input("정수입력"))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", number_input_a * number_input_a)
except Exception as e:
    print("type(Exception)", type(e))
    print("Exception", e)
    print("Exception", e.args[0])