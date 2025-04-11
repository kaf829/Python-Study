class CustomException(Exception):
    def __init__(self,message,value):
        super().__init__()
        self.message = message
        self.value = value

    def __str__(self):
        return self.message

    def print(self):
        print("####오류정보")
        print("a메세지", self.message)
        print("value ", self.value)

try:
    raise CustomException("딱히 이유 없음", 273)
except CustomException as e:
    e.print()