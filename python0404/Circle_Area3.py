
pi = 3.14


def circle_area(r):
    global pi #global로 선언하지 않으면 전역변수를 내부에서 똑같은 변수이름으로 사용 못함
    pi = pi + 0.0015
    x = 20
    result = pi * (r**2)
    return result


if __name__ == "__main__":
    print("PI:", pi)
    print("반지름:", 3 ,"면적", circle_area(3))
    print("PI", pi)