class Parents:
    def __init__(self):
        self.value = "테스트"
        print("parents 클래스의 __init__메서드가 호출되었습니다")

    def test(self):
        print("parents 클래스의 test()메소드입니다")


class Child(Parents):
    def __init__(self):
        super().__init__()
        print("child 클래스에서 초기확가 됨")



child = Child()
child.test()
print(child.value)