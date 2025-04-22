import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# 데이터 로드
df = pd.read_csv('../merged_car_prices_cpi.csv')
plt.rcParams['font.family'] = 'Malgun Gothic'

# 2x2 서브플롯 생성
fig, ax = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('지역별 CPI 단위당 판매량 변화', fontsize=16)

# 지역별 분석
slopes = {}  # 기울기 저장 딕셔너리
for idx, (region, group) in enumerate(df.groupby('region')):
    # 월별 판매량 및 CPI 계산
    monthly_data = group.groupby(['year', 'month']).agg(
        sales_volume=('sellingprice', 'count'),
        cpi=('cpi', 'mean')
    ).reset_index()

    # 회귀분석으로 기울기 계산
    slope, intercept, _, _, _ = linregress(monthly_data['cpi'], monthly_data['sales_volume'])
    slopes[region] = slope  # 기울기 저장

    # 서브플롯 위치 계산
    row = idx // 2
    col = idx % 2

    sns.regplot(
        data=monthly_data,
        x='cpi',
        y='sales_volume',
        ax=ax[row, col],
        scatter=False,
        color='red',
        line_kws={'label': f'기울기: {slope:.2f}'}
    )

    # 그래프 설정
    ax[row, col].set_title(f'{region} 지역', pad=15)
    ax[row, col].set_xlabel('CPI')
    ax[row, col].set_ylabel('월별 판매량')
    ax[row, col].grid(True)
    ax[row, col].legend()

plt.tight_layout()
plt.subplots_adjust(top=0.92)
plt.show()

# 기울기 결과 출력
print("\n[ 지역별 CPI 0.1단위 증가당 판매량 변화 ]")
for region, slope in slopes.items():
    print(f"- {region}: {slope*0.1:.2f}대 감소")
