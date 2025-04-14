import time

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))




# from datetime import datetime
#
# # 특정 날짜와 시간 설정
# date_time_str = datetime.now()
# print(datetime.now)
# date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
#
# print("The date and time is:", date_time_obj)
