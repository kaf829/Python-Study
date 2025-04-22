import pandas as pd

# 파일 로드
df = pd.read_csv('C:/Users/MINJUN/Desktop/data/car_prices.csv')


df['saledate'] = pd.to_datetime(df['saledate'], utc=True, errors='coerce')
df['year'] = df['saledate'].dt.year
df['month'] = df['saledate'].dt.month


state_to_region = {
    'CA': 'West', 'TX': 'South', 'PA': 'Northeast', 'MN': 'Midwest',
    'AZ': 'West', 'WI': 'Midwest', 'TN': 'South', 'MD': 'South',
    'FL': 'South', 'NE': 'Midwest', 'NJ': 'Northeast', 'NV': 'West',
    'OH': 'Midwest', 'MI': 'Midwest', 'GA': 'South', 'VA': 'South',
    'SC': 'South', 'NC': 'South', 'IN': 'Midwest', 'IL': 'Midwest',
    'CO': 'West', 'UT': 'West', 'MO': 'Midwest', 'NY': 'Nrtheast',
    'MA': 'Northeast', 'PR': 'South', 'OR': 'West', 'LA': 'South',
    'WA': 'West', 'HI': 'West', 'OK': 'South', 'MS': 'South',
    'NM': 'West', 'AL': 'South'
}


df['state'] = df['state'].str.upper()
df['region'] = df['state'].map(state_to_region)


cols = ['make', 'model', 'trim', 'body', 'vin', 'condition', 'odometer',
        'color', 'interior', 'seller', 'mmr', 'sellingprice', 'saledate',
        'year', 'month', 'transmission', 'state', 'region']
df = df[cols]


df.to_csv('car_prices_processed.csv', index=False, encoding='utf-8-sig')

print("데이터 변환 완료")

