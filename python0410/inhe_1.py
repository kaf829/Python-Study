class A:
    def __init__(self ,x):
        self.aa = x

    def printA(self):
        print(self.aa)

    def a_m(self):
        print("a_m")



class B(A):
    def __init__(self,x,y):
        super().__init__(x)
        self.bb = y

    def b_m(self):
        print("b_m")


    def printB(self):
        print(self.bb)


class C(B):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.cc = z

    def c_m(self):
        print("c_m")

    def printC(self):
        print(self.cc)
        print(self.bb)
        print(self.aa)




