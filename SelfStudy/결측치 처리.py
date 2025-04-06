import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, None, 35],
    'City': ['New York', 'Los Angeles', None]
}


df = pd.DataFrame(data)

# 결측치 확인 => null인 값은 true 아닌값은 false
print(df.isnull())

# # 결측치 제거 => 하나라도 NONE이 있으면 그 로우는 안나옴
df_dropped = df.dropna()
print(df_dropped)

# # 결측치 채우기 => filna => None인 값 삽인해주는거, mean()은 평균을 구하는 거고
df_filled = df.fillna({'Age': df['Age'].mean(), 'City': 'Unknown'})
print(df_filled)
