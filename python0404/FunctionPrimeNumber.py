def input_num():
    num1 = int(input("첫번째 숫자:"))
    num2 = int(input("두번째 숫자"))
    return num1,num2


def calc_min_max(num1,num2):
    min_num = min(num1, num2)
    max_num = max(num1, num2)
    return min_num,max_num

def print_number(num1,num2):
    result = []
    for i in range(num1, num2 + 1):
        if i < 2:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.append(i)

    for index, value in enumerate(result):
        if index % 10 == 0:
            print("\n")
        print(value, end=' ')

    print()
    print("갯수:", len(result))


num1,num2 = input_num()
min_number, max_number = calc_min_max(num1,num2)
print_number(min_number,max_number)




