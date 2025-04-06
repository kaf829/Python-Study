import pandas as pd

# CSV 파일 읽기
df = pd.read_csv('large_data.csv')
print(df)


# df.to_csv('output.csv', index=False)