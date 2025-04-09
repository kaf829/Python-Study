
list_a = ["52","273","32", "스파이", "193"]


list_number = []
list_string = []
for item in list_a:
    try:
        float(item)
        list_number.append(item)
    except:
        list_string.append(item)


print("{}내부에 있는 숫자".format(list_a))
print("{}입니다".format(list_number))
print("문자는 {}입니다".format(list_string))

