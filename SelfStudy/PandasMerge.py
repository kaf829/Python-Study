import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 4],
    'Age': [25, 30, 40]
})

merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)