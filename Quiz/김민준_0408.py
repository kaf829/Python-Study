class User_Exception(Exception):
    def __init__(self, msg1):
        self._message1 = msg1

    def __str__(self):
        return self._message1


def list_isDigit(j_list):
    try:
        j_list = [i for i in j_list if i.isdigit()]

        if len(j_list) != 13:
            raise User_Exception("주민번호가 잘못되었습니다 숫자가 13개가 아닙니다")

        check_value = int(j_list.pop(-1))
        weight_value = [i - 7 if i > 9 else i for i in range(2, 15)]

        sum_data_list = 0

        for i in range(len(j_list)):
            sum_data_list += int(j_list[i]) * weight_value[i]

        result = 11 - (sum_data_list % 11)

        if result >= 10:
            result -= 10

        return result == check_value
    except User_Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    while True:
        jumin = input("주민번호를 입력하세요: ")
        result = list_isDigit(jumin)
        if result:
            jumin += "(O)"
            print(f"{jumin}")
        else:
            jumin += "(X)"
            print(f"{jumin}")
