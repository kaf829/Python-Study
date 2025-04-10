


class Person:
    def __init__(self):
        self._hakbun = ""
        self._irum = ""



    def printData(self):
        print(self._hakbun, self._irum)

    def set_hakbun(self,hakbun):
        self._hakbun = hakbun

    def get_hakbun(self,hakbun):
        return self._hakbun

    def set_irum(self,irum):
        self._irum = irum

    def get_irum(self, hakbun):
        return self._irum




obj = Person()
# obj.printData()

obj.set_hakbun("A001")
obj.set_irum("홍길동")

obj.printData()
print(obj)
del obj