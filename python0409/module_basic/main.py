import test_module as tm

print("메인의 __name__ 출력하기")
print(__name__)
print()

radius = tm.number_input()
print("원의 넓이" ,tm.get_circle_area(radius))
print("원의 둘레", tm.get_circle_meter(radius))
