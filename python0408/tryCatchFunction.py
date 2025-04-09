def some_function():
    print("1~10까지의 수를 입력하세요")
    num = int(input())
    if num < 1 or num > 10:
        raise Exception("유효하지 않은 숫자입니다:.{0}".format(num))
    else:
        print("입력한 수는 {0}입니다".format(num))

def some_function_caller():
    try:
        some_function()
    except Exception as error:
        print("(1)예외가 발생했습니다 {0}".format(error))
        raise # 상위 호출자에게 해당 에러를 던져주고 싶을때 그냥 raise 라고 쓰면 됨

try:
    some_function_caller()
except Exception as e:
    print("(2) 예외가 발생하였습니다 {0}".format(e))