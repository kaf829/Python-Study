import zipfile
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# 데이터 불러오기
df = pd.read_csv('../merged_car_prices_cpi.csv')

# 지역, 연도, 월별 판매량(거래 건수)과 CPI 평균 계산
grouped = df.groupby(['region', 'year', 'month']).agg(
    sales_volume=('sellingprice', 'count'),
    cpi=('cpi', 'mean')
).reset_index()

# 지역별 산점도와 경향선(회귀선) 그리기
g = sns.FacetGrid(grouped, col='region', col_wrap=2, height=4, aspect=1.2)
g.map_dataframe(sns.scatterplot, x='cpi', y='sales_volume', alpha=0.7)
g.map_dataframe(sns.regplot, x='cpi', y='sales_volume', scatter=False, line_kws={'color':'red'})
g.set_axis_labels('CPI', '판매량')
g.fig.suptitle('지역별 CPI와 판매량의 관계', y=1.05, fontsize=16)
plt.tight_layout()
plt.show()
