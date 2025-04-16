import pandas as pd

data = {
    "2020": [1000000, 2000000, 3000000, 4000000],
    "2015": [900000, 1800000, 2700000, 3600000],
    "지역": ["서울", "부산", "인천", "대구"]
}
df = pd.DataFrame(data)


df.index.name = "지역"
df.index = df["지역"]
print(df)

print("-------------------")

data = {
    "2020": [1000000, 2000000, 3000000, 4000000],
    "2015": [900000, 1800000, 2700000, 3600000],
    "지역": ["서울", "부산", "인천", "대구"]
}
df = pd.DataFrame(data)

df.rename(columns = {"2020": "2020년 인구"}, inplace=True)
df.rename(columns = {"2015": "2015년 인구"}, inplace=True)

print(df)

print("-" * 80)

df['2020년 인구'] = [i + (i * 0.1)  for i in df["2020년 인구"]]
print(df)

print("-----------------------------------")
index_list = ["A", "B", "C", "D"]
df = pd.DataFrame(data, index=index_list)
df.drop(index = "C", inplace=True)
print(df)

