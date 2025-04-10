import random
print("# random")

print(" -random()", random.random())
print(" -uniform(10,20)", random.uniform(10,20))
print(" -randrange(10,20)", random.randrange(10))
print(" -choice([1,2,3,4,5,])", random.choice([1,2,3,4,5]))
numbers = [1,2,3,4,5]
print(" -random.shuffle([1,2,3,4,5])", random.shuffle(numbers))
print(numbers)
print(" -sample([1,2,3,4,5],3))", random.sample([1,2,3,4,5],3))


