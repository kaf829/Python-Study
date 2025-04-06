import pandas as pd


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
    'Month': ['Jan', 'Jan', 'Jan', 'Feb', 'Feb'],
    'Sales': [100, 200, 300, 400, 500]
}

df = pd.DataFrame(data)
pivot_table = df.pivot_table(values='Sales', index='Name', columns='Month', aggfunc='sum')
print(pivot_table)