import pandas as pd
data={'empnum':[1, 2, 3, 4],
    'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
      'Age':[27, 24, 22, 32],
      'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],}
df=pd.DataFrame(data)
print(df)
df['salary']=[10000,20000,30000,40000]
print(df)
df['designation']=['intern','jr. developer','sr. developer','manager']
print(df)
)