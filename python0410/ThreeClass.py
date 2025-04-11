class A:
    def __init__(self):
        self.aa = 10

    def printA(self):
        print(self.aa)


class B(A):
    def __init__(self):
        super().__init__()
        self.bb =20


    def printB(self):
        print(self.bb)


class C(B):
    def __init__(self):
        super().__init__()
        self.cc = 30

    def printC(self):
        print(self.cc)
        print(self.bb)
        print(self.aa)




test = C()
test.printC()