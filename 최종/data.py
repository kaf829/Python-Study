
import pandas as pd

file_path = "C:/Users/MINJUN/Desktop/data/car_prices.csv"
df = pd.read_csv(file_path)


df = df[df['condition'].notna()]
# car = car[car['condition'].str.strip() != ""]

df = df.dropna(subset=['model'])
df = df[df['model'].str.strip() != ""]

df = df.dropna(subset=['make'])
df = df[df['make'].str.strip() != ""]
df = df[~df['model'].apply(lambda x: str(x).isdigit())]

df = df.dropna(subset = ['interior'])
df = df[df['interior'].str.strip() != '']
df = df[~df['interior'].apply(lambda x: x == "-")]

df = df.dropna(subset = ['color'])
df = df[df['color'].str.strip() != ""]
df = df[~df['color'].apply(lambda x: x == "-")]


df['make'] = df['make'].replace('nissan', 'Nissan')
df['make'] = df['make'].replace('ford truck', 'Ford')
df['make'] = df['make'].replace('ford tk', 'Ford')
df['make'] = df['make'].replace('chevrolet', 'Chevrolet')
df['make'] = df['make'].replace('chev truck', 'Chevrolet')
df['make'] = df['make'].replace('toyota', 'Toyota')
df['make'] = df['make'].replace('kia', 'Kia')
df['make'] = df['make'].replace('toyota', 'Nissan')
df['make'] = df['make'].replace('hyundai', 'Hyundai')
df['make'] = df['make'].replace('bmw', 'BMW')
df['make'] = df['make'].replace('chrysler', 'Chrysler')
df['make'] = df['make'].replace('mercedes', 'Mercedes-Benz')
df['make'] = df['make'].replace('mercedes-b', 'Mercedes-Benz')
df['make'] = df['make'].replace('jeep', 'Jeep')
df['make'] = df['make'].replace('volkswagen', 'Volkswagen')
df['make'] = df['make'].replace('lexus', 'Lexus')
df['make'] = df['make'].replace('gmc', 'GMC')
df['make'] = df['make'].replace('gmc truck', 'GMC')
df['make'] = df['make'].replace('mazda', 'Mazda')
df['make'] = df['make'].replace('cadillac', 'Cadillac')
df['make'] = df['make'].replace('acura', 'Acura')
df['make'] = df['make'].replace('audi', 'Audi')
df['make'] = df['make'].replace('lincoln', 'Lincoln')
df['make'] = df['make'].replace('subaru', 'Subaru')
df['make'] = df['make'].replace('buick', 'Buick')
df['make'] = df['make'].replace('pontiac', 'Pontiac')
df['make'] = df['make'].replace('mitsubishi', 'Mitsubishi')
df['make'] = df['make'].replace('mercury', 'Mercury')
df['make'] = df['make'].replace('land rover', 'Land Rover')
df['make'] = df['make'].replace('porsche', 'Porsche')
df['make'] = df['make'].replace('suzuki', 'Suzuki')
df['make'] = df['make'].replace('oldsmobile', 'Oldsmobile')
df['make'] = df['make'].replace('dodge', 'Dodge')
df['make'] = df['make'].replace('dodge tk', 'Dodge')
df['make'] = df['make'].replace('vw', 'Volkswagen')


df['model'] = df['model'].str.lower()
df['model'] = df['model'].str.strip()



canada = ['QC','AB','ON','NS']
df_trans = df.transmission.map(lambda x: None if x == 'Sedan' or x ==  'sedan' else x)
df_state = df.state.map(lambda x: None if x in canada or len(x) >= 6 else x)
df.drop(['transmission','state'], axis = 1 , inplace = True)
df['transmission'] = df_trans
df['state'] = df_state


df.to_csv(file_path, index=False)