import pandas as pd
import numpy as np

# 1. 데이터 불러오기
df = pd.read_csv("state_cpi_data.csv")

# 2. 모든 state-year-month 조합 생성 (1~12월)
all_months = pd.DataFrame(
    [(state, year, month)
     for state in df['state'].unique()
     for year in df[df['state'] == state]['year'].unique()
     for month in range(1, 13)],
    columns=['state', 'year', 'month']
)

# 3. 원본 데이터와 병합
merged = pd.merge(all_months, df, on=['state', 'year', 'month'], how='left')

# 4. 결측치 보완 함수
def fill_group(group):
    group = group.sort_values('month').reset_index(drop=True)
    cpi = group['CPI'].values.astype(float)
    for i in range(12):
        if np.isnan(cpi[i]):
            # 1월 결측: 2월 값 사용
            if i == 0:
                if not np.isnan(cpi[1]):
                    cpi[i] = cpi[1]
                    print(f"{group['state'][0]} {group['year'][0]}년 1월 → 2월 값({cpi[1]})로 대체")
            # 12월 결측: 11월 값 사용
            elif i == 11:
                if not np.isnan(cpi[10]):
                    cpi[i] = cpi[10]
                    print(f"{group['state'][0]} {group['year'][0]}년 12월 → 11월 값({cpi[10]})로 대체")
            # 2~11월 결측: 양쪽 값 평균, 한쪽만 있으면 그 값
            else:
                prev = cpi[i-1] if not np.isnan(cpi[i-1]) else None
                next_ = cpi[i+1] if not np.isnan(cpi[i+1]) else None
                if prev is not None and next_ is not None:
                    cpi[i] = round((prev + next_) / 2, 2)
                    print(f"{group['state'][0]} {group['year'][0]}년 {i+1}월 → {i}월({prev})과 {i+2}월({next_})의 평균({cpi[i]})로 대체")
                elif prev is not None:
                    cpi[i] = prev
                    print(f"{group['state'][0]} {group['year'][0]}년 {i+1}월 → {i}월 값({prev})로 대체")
                elif next_ is not None:
                    cpi[i] = next_
                    print(f"{group['state'][0]} {group['year'][0]}년 {i+1}월 → {i+2}월 값({next_})로 대체")
    group['CPI'] = cpi
    return group

# 5. state-year별로 결측치 보완 적용
filled = merged.groupby(['state', 'year'], group_keys=False).apply(fill_group).reset_index(drop=True)

# 6. 결과 저장
filled.to_csv("filled_state_cpi_data.csv", index=False)
print("완성된 데이터가 'filled_state_cpi_data.csv'에 저장되었습니다.")
