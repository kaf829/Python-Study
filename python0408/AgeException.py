


class AgeException(Exception):
    def __init__(self, msg1, msg2= ''):
        self._message1 = msg1
        self._message2 = msg2


def input_age():
    age = int(input("나이를 입력하세요"))

    if age < 0:
        raise AgeException("나이는 음수가 될 수 없습니다")
    elif age > 150:
        raise AgeException("150세 이상 살 수 있을까요?", "흠")
    else:
        return age


if __name__ == "__main__":
    try:
        age = input_age()
    except Exception as e:
        print(e.args)
    else:
        print(f"나이는 {age}세 입니다")