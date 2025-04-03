output = ""

for i in range(1,10):
    for j in range(0, i):
        output += "*"
    output += "\n"

print(output)



for i in range(1,10):
    for j in range(0, i):
        output += "*"
        print("i= ", i, ", j = ", j)
    output += '\n'

print(output)