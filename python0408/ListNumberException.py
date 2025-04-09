list_number= [52,273,73,100,52]

try:
    number_input_a = int(input("정수 입력"))
    print(f"{number_input_a}번쨰 요소 {list_number[number_input_a]}")
    print(3/0)
except ValueError as value_e:
    print("type(Exception)", type(value_e))
    print("Exception", value_e)
except IndexError as index_e:
    print("type(Exception)", type(index_e))
    print("Exception", index_e)
except Exception as e:
    print("type(Exception)", type(e))
    print("Exception", e)
