
import pandas as pd
data={'product':['umbrella','matterss','badminaton','shuttle'],
      'price':[1250,1450,1550,400],
      'dis':[10,8,15,10]}
df=pd.DataFrame(data)
print("original dataframe",df)
df['color']=['red','blue','green','yellow']
print("after adding color column",df)
print("displaying only product column")
print(df['product'])
print("displaying product name having discount value>10")
print(df[df['dis']>10]['product'])