import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)
print("-"*50)
print(df['Name'])
print("-"*50)
print(df.iloc[0])  # 첫 번째 행 선택

print("-"*50)
filtered_df = df[df['Age'] > 30]
print(filtered_df)