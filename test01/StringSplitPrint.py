number = input("정수입력")
number = int(number)

if number % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")


while True:
    if number > 90:
        print("A")
        break
    if number > 80:
        print("B")
        break
    if number > 70:
        print("C")
        break
    if number > 60:
        print("D")