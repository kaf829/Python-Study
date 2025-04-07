import random


print(random.random())
print("1----------------------")
print(random.uniform(1,10))
print("2----------------------")
print(random.randint(1,10))
print("3----------------------")
print(random.randrange(0,100,2))
print("4----------------------")
print(random.choice('abcdefghk'))
print("5----------------------")
print(random.sample([1,2,3,4,5],3))
print("6----------------------")

items = [1,2,3,4,5,6,7]
random.shuffle(items)
print(items)
