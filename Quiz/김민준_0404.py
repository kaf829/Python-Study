# [문제1] 덧셈, 뺄셈, 곱셈, 나눗셈을 수행해주는 프로그램을 작성하시오. 원하는 연산의 번호를 입력 후, 두 개의 양의 정수를 입력하면 연산 결과를 출력해준다.
# 만약, 각 연산에 배정된 숫자가 아닌 다른 숫자를 입력하면 잘못 입력하였다는 정보를 출력하여야 한다.
# <처리조건>
# 1. 원하는 연산의 번호는 1.덧셈 2.뺄셈 3.곱셈 4.나눗셈으로 한다.
# 2. 덧셈, 뺄셈, 곱셈, 나눗셈을 수행하는 부분은 각각 함수로 작성한다.
def sumCalc(num1, num2):
    print(f"{num1} + {num2} = ", num1 + num2)

def minusCalc(num1,num2):
    print(f"{num1} - {num2} =  ", num1 - num2)

def multiCalc(num1,num2):
    print(f"{num1} * {num2} =  ", num1 * num2)


def divideCalc(num1,num2):
    print(f"{num1} / {num2} =  ", num1/num2)



def calculator():
    print("원하는 연산의 번호는 1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 입니다")
    choice = int(input("숫자를 입력해주세요"))

    num1 = int(input("첫번쨰 숫자 =>"))
    num2 = int(input("두번쨰 숫자 =>" ))

    if num1 <= 0 and num2 <=0:
        return print("두 수가 모두 양수여야 합니다!!")

    if choice == 1:
        sumCalc(num1, num2)
    if choice == 2:
        minusCalc(num1,num2)
    if choice == 3:
        multiCalc(num1,num2)
    if choice == 4:
        divideCalc(num1,num2)


# calculator()


# [문제2] 세 개의 양의 정수를 입력 받아 그 합이 짝수이면 가장 큰 수를 출력(내부함수 사용X)하고, 홀수이면 그냥 그 합을 출력하는 프로그램을 작성하시오.

def even_odd_calc():

    numbers = [int(input("첫번째 숫자")),int(input("두번째 숫자")),int(input("세번째 숫자"))]
    sum_number = 0
    even_max = 0

    for num in numbers:
        sum_number += num
        if even_max <= num:
            even_max = num

    if sum_number % 2 == 0:
        print(f"세 수의 합은 짝수이고, 가장 큰 수는 {even_max}")
    else:
        print(f"세 수의 합은 홀수이고, 합은 {sum_number}")



# even_odd_calc()




# [문제3] 1이상의 정수를 입력하면 그 수의 약수를 출력해주는 프로그램을 for문을 이용해 작성하시오.
def factors_numer():
    num = int(input("1이상의 정수를 입력:"))

    if num <=0:
        return print("1이상의 수를 입력하세요")

    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)

    print(f"{num} 의 약수",result)

factors_numer()