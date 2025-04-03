list_a = [1,2,3,4,5]

del list_a[1]
print(list_a)

res = list_a.pop(2)
print("pop(2):", res)
print(list_a)


print("pop():", list_a.pop())
print("pop():", list_a.pop())