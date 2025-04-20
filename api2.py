import requests
import pandas as pd
import json

# BLS API 키 (BLS에서 발급받은 키를 입력)
api_key = "9860da1f6a0b684a6d4e7db130cd1073"

# 주 목록 (주별 코드)
states = [
    "CA", "TX", "PA", "MN", "AZ", "WI", "TN", "MD", "FL", "NE", "NJ", "NV",
    "OH", "MI", "GA", "VA", "SC", "NC", "IN", "IL", "CO", "UT", "MO", "NY",
    "MA", "PR", "OR", "LA", "WA", "HI", "OK", "MS", "NM", "AL"
]

# BLS API 기본 URL
bls_url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"

# 데이터를 저장할 리스트
data_list = []

# BLS 시리즈 ID 형식 예시: "CUUR0000SA0" + 주 코드
for state in states:
    series_id = f"CUUR0000SA0{state}"  # 각 주별 시리즈 ID 생성
    params = {
        "registrationKey": api_key,
        "seriesid": [series_id],
        "startyear": "1985",
        "endyear": "2015"
    }

    headers = {
        "Content-Type": "application/json"  # 요청 콘텐츠 유형을 JSON으로 설정
    }

    # API 호출
    response = requests.post(bls_url, headers=headers, data=json.dumps(params))

    if response.status_code == 200:
        data = response.json()

        if "Results" in data and "series" in data["Results"]:
            for observation in data["Results"]["series"]:
                if observation.get("data"):
                    for value in observation["data"]:
                        # 데이터 리스트에 주별, 날짜, CPI 값 추가
                        data_list.append({
                            'state': state,
                            'date': value['year'] + '-' + value['periodName'],
                            'value': value['value']
                        })
                else:
                    print(f"No data available for series_id {series_id} for {state}")
        else:
            print(f"No results found for {state} with series_id {series_id}")

    else:
        print(f"Failed to retrieve data for {state}: {response.status_code}")

# DataFrame으로 변환
df = pd.DataFrame(data_list)

# CSV로 저장
df.to_csv("state_cpi_data_bls.csv", index=False)

print("데이터가 CSV로 저장되었습니다.")
