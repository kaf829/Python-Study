import datetime

print("현재 시간 출력하기")
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()


print("#시간을 포맷에 맞쳐 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
output_c = "{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.strftime("%Y"), now.strftime("%m"), now.strftime("%d"),
    now.strftime("%H"), now.strftime("%M"), now.strftime("%S")
)
print(output_a)
print(output_b)
print(output_b)
print()
