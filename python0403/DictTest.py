example_list = {1: "요소A", 2: "요소B", 3: "요소C"}

print("#딕셔너리 items() 함수로 출력")
print('itmes():', example_list.items())
print()

print("#반복문과 조합하기")
for i, value in example_list.items():
    print(f"{i}번째 요소는 {value}입니다")
