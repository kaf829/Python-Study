
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv('../merged_car_prices_cpi.csv')


sales_volume = df.groupby(['region', 'year', 'month']).size().reset_index(name='sales_volume')


cpi_avg = df.groupby(['region', 'year', 'month'])['cpi'].mean().reset_index()


merged = pd.merge(sales_volume, cpi_avg, on=['region', 'year', 'month'])

print(merged)

corr_by_region = merged.groupby('region').apply(lambda x: x['cpi'].corr(x['sales_volume']))

print('지역별 CPI와 차량 판매량 상관계수:')
print(corr_by_region)


plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(8, 5))
sns.barplot(x=corr_by_region.index, y=corr_by_region.values, palette='viridis')
plt.title('지역별 CPI와 차량 판매량 상관계수')
plt.xlabel('지역')
plt.ylabel('상관계수')
plt.show()
