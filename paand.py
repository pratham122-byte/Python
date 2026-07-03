import pandas as pd
data={'empnum': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df=pd.DataFrame(data)
print(df)
print(df.head())
print(df.tail())
#print(df.describe())
print(df.info())
#selecting columns
ages=df['Age']
print(ages)
names=df['Name']
print(names)