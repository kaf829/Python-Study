# import pandas as pd
#
#
# file_path = "C:/Users/MINJUN/Desktop/data/car_prices.csv"
# car = pd.read_csv(file_path)
#
# # condition 컬럼의 값이 빈값인 로우 삭제
# car = car[car['condition'].notna()]
# car = car[car['saledate'].notna() | (car['saledate'] != '')]
# car = car[pd.to_numeric(car['sellingprice'], errors='coerce').notna()]
#
#
#
#
# car.to_csv(file_path, index=False)
import pandas as pd


# 출력 설정 변경 (전체 컬럼, 전체 행 보기)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

file_path = "C:/Users/MINJUN/Desktop/data/car_prices.csv"
car = pd.read_csv(file_path)


# null_rows = car[car['saledate'].isnull() | (ccalar['saledate'] == '')]
# null_rows = car[car.iloc[97]]



car = pd.DataFrame(car)

# model 열의 값에 "월" 글자가 포함된 행 필터링

filtered_rows = car[car['model'].str.contains('[가-힣]', na=False)]
print(filtered_rows)





# print(null_rows)

# condition 컬럼의 값이 빈값인 로우 삭제

# car = car[pd.to_numeric(car['sellingprice'], errors='coerce').notna()]


# print(car)
