class Car:
    def __init__(self):
        self.__price = 2000
        self.__speed = 0
        self.__color = "red"

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_speed(self):
        return self.__speed

    def set_spped(self,speed):
        self.__speed = speed

    price = property(get_price,set_price)
    color = property(get_color,set_color)


if __name__ == "__main__":
    my_car = Car()
    my_car.set_price(2000)
    my_car.set_spped(20)
    my_car.set_color('red')

    print("가격", my_car.get_price)
    print("속도", my_car.get_speed)
    print("색상", my_car.get_color)

    my_car.price = 20000
    my_car.speed = 200
    my_car.color = 'blue'
    print("가격:", my_car.price)
    print("속도:", my_car.speed)
    print("색상:", my_car.color)