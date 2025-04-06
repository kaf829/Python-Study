# *** 4월 3일 ***
# [문제1] 0이 아닌 두수를 곱할때 (양수)* (양수), (음수)*(음수) 일떄는 양수가 되고 (양수)*(음수) 또는 (음수)*(양수) 일때는 음수 가 된다.
# 두수를 입력받아 부호를 판별하는 프로그램을 작성하시오.

def number_confirm():
    a = int(input("수를 입력하세요:"))
    b = int(input("수를 입력하세요: "))
    if(a == 0) or b == 0 : return print("0이 아닌 수를 입력하세요")

    if a > 0 and b > 0:
        return print("두 수의 곱은 양수이다")
    elif a < 0 and b < 0:
        return print("두 수의 곱은 양수이다")
    else:
        return print("두 수의 곱은 음수이다")


number_confirm()


# [문제2] 학생수준평가 시험에서 영어점수와 수학점수가 합해서 110점이 넘으면 합격이지만 각 점수가 40점 미만이면 불합격이 다.
# 영어점수와 수학점수를 입력받아 힙격여부를 출력하는 프로그램을 작성하시오.


def cutline_score():
    eng = int(input("영어점수를 입력하세요"))
    math = int(input("수학점수를 입력하세요"))

    if eng < 40 or math < 40:
        return print("불합격입니다")

    if eng + math > 110:
        print("합격입니다")
    else:
        print("불합격입니다")


# cutline_score()



# [문제3] 공을 일정 높이에서 던졌을 때, 원래의 높이의 1/만큼 튀어 오른다고 한다. 그러다가 높이가 0.00001m보다 낮으면 튀어 오르지 않는다.
# 공을 던진 높이를 입력받은 후 while문을 이용해서 공이 튀어 오르지 않을때까지 공이 튀긴 횟수를 구해서 출력하시오.

def height_calc():
    height = float(input("높이를 입력하세요:"))
    count = 0
    while height > 0.00001:
        count +=1
        height = height/2

    print(count)


# height_calc()
