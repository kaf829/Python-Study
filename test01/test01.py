print("hello Python"); print("test")

import keyword

print(keyword.kwlist)


class Person:
    def __init__(self):
        self.a = 10
        self._b = 20 #강제접근은 가능하나  접근하지말라고 설계된 식별자
        self.__c = 30 #__은 private로 은닉화되어 있음 외부접근X


obj = Person()
print(obj.a)
print(obj._b)





