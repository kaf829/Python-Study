import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
df = pd.read_csv('../merged_car_prices_cpi.csv')
plt.rcParams['font.family'] = 'Malgun Gothic'

# 2x2 서브플롯 생성
fig, ax = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('지역별 CPI 증가당 판매량 변화', fontsize=16)
plt.rcParams['axes.unicode_minus'] = False
# 지역별 분석
slopes = {}  # 기울기 저장 딕셔너리
for idx, (region, group) in enumerate(df.groupby('region')):
    # 월별 판매량 및 CPI 계산
    monthly_data = group.groupby(['year', 'month']).agg(
        sales_volume=('sellingprice', 'count'),
        cpi=('cpi', 'mean')
    ).reset_index()

    # 공분산과 분산으로 기울기 계산
    x = monthly_data['cpi']
    y = monthly_data['sales_volume']
    n = len(x)

    # 평균 계산
    x_mean = x.mean()
    y_mean = y.mean()

    # 공분산
    covariance = ((x - x_mean) * (y - y_mean)).sum() / (n - 1)

    # 분산
    variance_x = ((x - x_mean) ** 2).sum() / (n - 1)

    # 기울기
    slope = covariance / variance_x
    slopes[region] = slope

    # 서브플롯 위치 계산
    row = idx // 2
    col = idx % 2

    # 산점도 + 추세선
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

# 기울기 결과 출력 (0.1단위 기준)
print("\n[ 지역별 CPI 0.1단위 증가당 판매량 변화 ]")
for region, slope in slopes.items():
    print(f"- {region}: {slope * 0.1:.2f}대 감소")
