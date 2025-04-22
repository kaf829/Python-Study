import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
df = pd.read_csv('../merged_car_prices_cpi.csv')
plt.rcParams['font.family'] = 'Malgun Gothic'
# 연-월 컬럼 생성 (시계열 분석용)
df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))


grouped = df.groupby(['region', 'date'])['sellingprice'].mean().reset_index()

plt.figure(figsize=(16, 7))
sns.lineplot(data=grouped, x='date', y='sellingprice', hue='region')
plt.title('지역별 평균가격')
plt.xlabel('일수')
plt.ylabel('평균 판매 가격')
plt.legend(title='지역')
plt.show()
