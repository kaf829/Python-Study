PI = 3.141592

def number_input():
    output  = input("숫자입력")
    return  float(output)


def get_circle_meter(radius):
    return 2 * PI * radius


def get_circle_area(radius):
    return PI * radius**2


if __name__ == "__main__":
    print("Test_Module의 __name__ 출력하기")
    print(__name__)
    print()

