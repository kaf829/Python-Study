import pandas as pd
# 경로 지정
base_path = "C:/Users/MINJUN/Desktop/welmart"

# 파일 불러오기
train_df = pd.read_csv(f"{base_path}/train.csv")
test_df = pd.read_csv(f"{base_path}/test.csv")
features_df = pd.read_csv(f"{base_path}/features.csv")
stores_df = pd.read_csv(f"{base_path}/stores.csv")

# 첫 5개 행 미리 보기
print("▶ train.csv")
print(train_df.head())

print("\n▶ test.csv")
print(test_df.head())

print("\n▶ features.csv")
print(features_df.head())

print("\n▶ stores.csv")
print(stores_df.head())


# 각 파일의 행/열 수 확인
print("Train Shape:", train_df.shape)
print("Test Shape:", test_df.shape)
print("Features Shape:", features_df.shape)
print("Stores Shape:", stores_df.shape)

# 결측치 있는 컬럼 확인
print("\nMissing values (train):\n", train_df.isnull().sum())
print("\nMissing values (features):\n", features_df.isnull().sum())

