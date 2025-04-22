import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
df = pd.read_csv('../merged_car_prices_cpi.csv')
plt.rcParams['font.family'] = 'Malgun Gothic'


plt.figure(figsize=(12, 7))
scatter = sns.scatterplot(
    data=df.sample(5000, random_state=42),
    x='cpi',
    y='sellingprice',
    hue='region',
    alpha=0.6,
    palette='viridis'
)


correlation = df[['cpi', 'sellingprice']].corr().iloc[0,1]
plt.text(0.05, 0.95, f'상관계수: {correlation}',
         transform=plt.gca().transAxes, fontsize=12)

plt.title('CPI vs 차량가격 (지역별 분포)', fontsize=14)
plt.xlabel('CPI', fontsize=12)
plt.ylabel('판매가격(USD)', fontsize=12)
plt.legend(title='지역', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()



monthly_corr = df.groupby('month')[['cpi','sellingprice']].corr().unstack()['cpi']['sellingprice']

plt.figure(figsize=(10, 6))
sns.heatmap(
    monthly_corr.to_frame().T,
    annot=True,
    cmap='coolwarm',
    vmin=-1,
    vmax=1,
    linewidths=0.5,
    cbar_kws={'label': '상관계수'}
)
plt.title('월별 CPI-가격 상관관계', pad=20)
plt.xlabel('월')
plt.yticks([])
plt.show()
