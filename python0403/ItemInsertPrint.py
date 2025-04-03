from tabulate import tabulate

data = []
while True:
    dict_data = {}  # 반복문 안에서 새로운 딕셔너리 생성
    item_no = input("제품번호 => ")
    if item_no.upper() == "EXIT":
        break
    dict_data["item_no"] = item_no
    dict_data["item_name"] = input("제품이름 => ")
    count = int(input("수량 => "))
    dict_data["count"] = count
    price = int(input("가격 => "))
    dict_data["price"] = price
    dict_data["total_price"] = count * price

    data.append(dict_data)

result = []
for i in range(len(data)):
    value = [value for value in data[i].values()]
    result.append(value)

print("\t\t\t\t\t\t\t ***영수증***")
print("-"*50)
print(tabulate(result, headers=["제품번호", "제품명", "수량", "단가", "금액"], stralign="center", tablefmt="plain"))

tot_sum = 0
for i in range(len(result)):
    tot_sum += int(result[i][4])
print("총 금액", tot_sum)



