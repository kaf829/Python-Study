import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 파일을 읽어옴
df = pd.read_csv('../merged_car_prices_cpi.csv')
plt.rcParams['font.family'] = 'Malgun Gothic'  # 한글 폰트 설정
plt.rcParams['axes.unicode_minus'] = False
# 2x2 서브플롯(4개 그래프) 생성, 전체 타이틀 지정
fig, ax = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('지역별 CPI와 판매량 관계 분석', fontsize=16)

# 각 지역별로 반복
for idx, (region, group) in enumerate(df.groupby('region')):
    # 해당 지역의 연도/월별로 판매량(거래 건수)과 CPI 평균을 계산
    monthly_data = group.groupby(['year', 'month']).agg(
        sales_volume=('sellingprice', 'count'),  # 판매량: 거래 건수
        cpi=('cpi', 'mean')  # CPI 평균
    ).reset_index()

    # 2x2 서브플롯의 행, 열 위치 계산
    row = idx // 2
    col = idx % 2

    # 산점도(점 그래프)로 CPI와 판매량의 관계 시각화
    # sns.scatterplot(
    #     data=monthly_data,
    #     x='cpi',
    #     y='sales_volume',
    #     ax=ax[row, col],
    #     alpha=0.7,
    #     label='실제 데이터'
    # )
    # 추세선(회귀선) 추가 (산점도 위에 빨간 선)
    sns.regplot(
        data=monthly_data,
        x='cpi',
        y='sales_volume',
        ax=ax[row, col],
        scatter=False,
        color='red',
        line_kws={'label': '추세선'}
    )

    # CPI와 판매량의 상관계수 계산 (음수면 CPI↑→판매량↓)
    corr = monthly_data['cpi'].corr(monthly_data['sales_volume']).round(3)

    # 서브플롯 제목에 지역명과 상관계수 표시
    ax[row, col].set_title(
        f'{region} 지역\nCPI-판매량 상관계수: {corr}',
        pad=15
    )
    # x축, y축 라벨 지정
    ax[row, col].set_xlabel('CPI')
    ax[row, col].set_ylabel('월별 판매량')
    # 격자 표시
    ax[row, col].grid(True)
    # 범례 표시
    ax[row, col].legend()

# 그래프 레이아웃 자동 조정
plt.tight_layout()
# 전체 타이틀과 서브플롯 간격 조정
plt.subplots_adjust(top=0.92)
# 그래프 출력
plt.show()
