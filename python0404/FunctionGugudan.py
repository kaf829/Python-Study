def input_num():
    num1 = int(input("첫번째 숫자:"))
    num2 = int(input("두번째 숫자"))

    min_num = min(num1, num2)
    max_num = max(num1, num2)
    return min_num,max_num


def proc_gugudan(min_num, max_num):
    for num in range(min_num, max_num + 1):
        print(f" ** {num}단 **   ", end='')


    print()


    for i in range(1, 10):
        for num in range(min_num, max_num + 1):
            print(f" {num:2d} * {i:2d} = {num * i:2d}", end="")
        print()



if __name__ == "__main__":
    m_min_num, m_max_num = input_num()
    proc_gugudan(m_min_num,m_max_num)

