even_sum = 0
odd_sum = 0
for i in range(1,101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i


print(odd_sum)
print(even_sum)


