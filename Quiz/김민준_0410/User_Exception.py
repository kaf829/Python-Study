class User_Exception(Exception):
    def __init__(self, msg1, flag=0, msg2='', ):
        self._message1 = msg1
        self._message2 = msg2
        self.flag = flag



# 1번 해당 데이터 없음 2번: valueError 3번: 인덱스에러
    def __str__(self):
        if self.flag == 1:
            return f"데이터 유효성 에러: {self._message1} 의 데이터는 존재하지 않습니다"
        elif self.flag == 2:
            return f"데이터 타입,크기 에러 : {self._message1} {self._message2}"
        elif self.flag == 3:
            return f"데이터 중복 에러 : {self._message1}의 데이터는 존재합니다"