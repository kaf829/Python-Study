testInput = input("주민번호:")

data = testInput.split("-")

result = []
for i in range(2):
    for num in data[i]:
        result.append(num)


print(result)