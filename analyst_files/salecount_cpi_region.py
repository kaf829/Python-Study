import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# 2. CSV 파일 로드
file_path = '../merged_car_prices_cpi.csv'
df = pd.read_csv(file_path)

# 3. 지역별 CPI와 판매가격 상관계수 계산
region_corr = df.groupby('region').apply(lambda x: x['cpi'].corr(x['sellingprice']))

count_sale_sum = df.groupby('region').count()

# 4. 시각화
plt.figure(figsize=(8, 5))
sns.barplot(x=region_corr.index, y=region_corr.values, palette='viridis')
plt.title('지역별 CPI와 차량 판매가격 상관계수')
plt.xlabel('지역')
plt.ylabel('상관계수')
plt.ylim(0, 0.1)
plt.show()
