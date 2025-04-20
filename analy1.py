import pandas as pd
import zipfile
import os
import matplotlib.pyplot as plt

# 1. 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


file_path = "C:/Users/MINJUN/Desktop/data/car_prices.csv"
# 3. 데이터 불러오기
cpi_df = pd.read_csv("filled_state_cpi_data.csv")
car_df = pd.read_csv(file_path)

car_df['state'] = car_df['state'].str.upper()
cpi_df['state'] = cpi_df['state'].str.upper()

# 4. 차량 데이터 전처리
month_map = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6,
             'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}

# 날짜 파싱 오류 방지 코드 추가
def parse_date(row):
    try:
        parts = row['saledate'].split()
        return int(parts[3]), month_map[parts[1]]
    except:
        return None, None

car_df[['sale_year', 'sale_month']] = car_df.apply(parse_date, axis=1, result_type='expand')
car_df = car_df.dropna(subset=['sale_year', 'sale_month', 'sellingprice'])
car_df = car_df[car_df['state'].isin(['GA', 'NC', 'NM', 'NY'])]

# 5. 데이터 병합 및 분석
merged = pd.merge(
    car_df,
    cpi_df,
    left_on=['state', 'sale_year', 'sale_month'],
    right_on=['state', 'year', 'month'],
    how='inner'
)

# 6. 시각화 및 분석
plt.figure(figsize=(18, 12))

# (1) CPI vs 가격 산점도
plt.subplot(2,2,1)
for state in ['GA', 'NC', 'NM', 'NY']:
    temp = merged[merged['state'] == state]
    plt.scatter(temp['CPI'], temp['sellingprice'], alpha=0.4, label=state)
plt.title('CPI와 차량 가격 관계')
plt.xlabel('CPI')
plt.ylabel('가격($)')
plt.legend()

# (2) 시간별 평균 가격 추이
plt.subplot(2,2,2)
for state in ['GA', 'NC', 'NM', 'NY']:
    temp = merged[merged['state'] == state]
    trend = temp.groupby('sale_year')['sellingprice'].mean()
    plt.plot(trend.index, trend.values, marker='o', label=state)
plt.title('연도별 평균 가격 추이')
plt.xlabel('연도')
plt.ylabel('평균 가격($)')
plt.legend()

# (3) CPI 변화 추이
plt.subplot(2,2,3)
for state in ['GA', 'NC', 'NM', 'NY']:
    temp = merged[merged['state'] == state]
    cpi_trend = temp.groupby('sale_year')['CPI'].mean()
    plt.plot(cpi_trend.index, cpi_trend.values, marker='o', label=state)
plt.title('연도별 CPI 변화')
plt.xlabel('연도')
plt.ylabel('CPI')
plt.legend()

# (4) CPI 구간별 평균 가격
plt.subplot(2,2,4)
for state in ['GA', 'NC', 'NM', 'NY']:
    temp = merged[merged['state'] == state]
    bins = pd.qcut(temp['CPI'], 5)
    price_by_bin = temp.groupby(bins)['sellingprice'].mean()
    plt.plot(price_by_bin.index.astype(str), price_by_bin.values, marker='o', label=state)
plt.title('CPI 구간별 평균 가격')
plt.xlabel('CPI 구간')
plt.ylabel('평균 가격($)')
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()

# 7. 상관관계 분석
print("주별 상관관계:")
for state in ['GA', 'NC', 'NM', 'NY']:
    subset = merged[merged['state'] == state]
    corr = subset['sellingprice'].corr(subset['CPI'])
    print(f"{state}: {corr:.3f}")
