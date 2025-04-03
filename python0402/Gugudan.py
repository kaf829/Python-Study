num1 = int(input("첫번째 숫자:"))
num2 = int(input("두번째 숫자"))

min_num = min(num1,num2)
max_num = max(num1,num2)
for num in range(min_num,max_num+1):
    print(f" ** {num}단 **   ", end = '')

print()

for i in range(1,10):
    for num in range(min_num, max_num + 1):
     print(f" {num:2d} * {i:2d} = {num * i:2d}", end = "")
    print()
