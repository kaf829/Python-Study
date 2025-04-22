
import pandas as pd


# 2. 데이터 불러오기
df_car_prices = pd.read_csv('car_prices_processed.csv')
df_cpi = pd.read_csv('us_cpi_regions_1985_2015.csv')

# 3. region 컬럼 정규화 (예: 'west' → 'West')
df_car_prices['region'] = df_car_prices['region'].str.capitalize()

# 4. INNER JOIN
merged_df = pd.merge(
    df_car_prices,
    df_cpi,
    how='inner',
    left_on=['region', 'year', 'month'],
    right_on=['region', 'year', 'month']
)

# 5. CSV로 저장
merged_df.to_csv('merged_car_prices_cpi.csv', index=False, encoding='utf-8-sig')
