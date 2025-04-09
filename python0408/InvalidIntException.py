class InvalidIntException(Exception):
    def __inif__(self, arg):
        super().__init__('정수가 아닙니다: {0}'.format(arg))


def convert_to_integer(text):
    if text.isdigit():
        return int(text)
    else:
        raise InvalidIntException(text)


if __name__ == "__main__":
    try:
        text = input('숫자를 입력하세요')
        number = convert_to_integer(text)
    except InvalidIntException as e:
        print("예외가 발생하였습니다 ({0})".format(e))
    else:
        print("정수 형식으로 변환되었습니t다 {0} {1}".format(number,type(number)))