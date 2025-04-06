import pandas as pd
import numpy as np


date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')

df = pd.DataFrame(date_rng, columns=['date'])

df['data'] = np.random.randint(0, 100, size=(len(date_rng)))

print(df)
# 날짜를 인덱스로 설정
df.set_index('date', inplace=True)

# 일별 데이터 합계
daily_sum = df.resample('D').sum()
print(daily_sum)