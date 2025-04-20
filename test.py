import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 출력 설정 변경 (전체 컬럼, 전체 행 보기)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# CSV 불러오기
file_path = "C:/Users/MINJUN/Desktop/data/car_prices.csv"
car = pd.read_csv(file_path)

# 보기 좋게 출력
print("▶ car.csv 데이터")
#
# print(car)

# # state 컬럼이 'Sedan' 또는 'sedan'인 데이터만 필터링
# filtered_data = car[car['state'].str.lower().isin(['sedan'])]
#
# # 필터링된 데이터 출력
# print("▶ state 컬럼이 'Sedan' 또는 'sedan'인 데이터")
# print(filtered_data)



#car = car[car['vin'] != '5npe24af4fh001562']
#car = car[car['vin'] != "1g1pe5sbxe7120097"]
#car = car[car['vin'] != '2g1fb3d31e9134662']
#car = car[car['vin'] != '5npe24af4fh038482']
#car = car[car['vin'] != '5uxkr2c52e0h33130']
# car = car[car['vin'] != '5uxkr2c52e0h33130']


# car.loc[car['vin'] == '5npe24af4fh001562', 'saleDate'] = car.loc[car['vin'] == '5npe24af4fh001562', 'sellingprice']


print(car.loc[car['vin'] =='5npe24af4fh001562'])



# for col in car.columns:
#     print(f"\n🟡 {col} ({car[col].dtype})")
#     print(len(car[col].unique()))
#     print(car[col].unique())




import pandas as pd






# 수치형 컬럼만 추출
# numeric_df = car.select_dtypes(include=['number'])
#
# # 상관계수 계산
# correlation_matrix = numeric_df.corr()
#
# # 히트맵 시각화
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
# plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.show()
