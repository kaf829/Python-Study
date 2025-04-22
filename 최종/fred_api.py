import requests
import csv
from datetime import datetime

api_key = "9860da1f6a0b684a6d4e7db130cd1073"
regions = {
    "CUUR0100SA0": "Northeast",
    "CUUR0200SA0": "Midwest",
    "CUUR0300SA0": "South",
    "CUUR0400SA0": "West"
}
base_url = "https://api.stlouisfed.org/fred/series/observations"
start_date = "1987-01-01"
end_date = "2015-12-31"

rows = []

for series_id, region_name in regions.items():
    url = (
        f"{base_url}?series_id={series_id}"
        f"&api_key={api_key}&file_type=json"
        f"&observation_start={start_date}&observation_end={end_date}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for obs in data['observations']:
            date_str = obs['date']
            value = obs['value']
            # 날짜에서 년, 월 추출
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            year = dt.year
            month = dt.month
            # 결측값 처리
            if value == ".":
                continue
            rows.append([region_name, year, month, value])
    else:
        print(f"{region_name} (series ID: {series_id}) 데이터 조회 실패: {response.status_code}")

# CSV 파일로 저장
with open("us_cpi_regions_1985_2015.csv", "w", newline='', encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["region", "year", "month", "cpi"])
    writer.writerows(rows)

print("CSV 파일 저장 완료: us_cpi_regions_1985_2015.csv")
