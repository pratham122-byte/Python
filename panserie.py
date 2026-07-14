import pandas as pd
import numpy as np
a=[1,3,5,7,9]
myvar=pd.Series(a,index=["a","b","c","d","e"])
print(myvar)
ser=pd.Series() 
print("panda empty series",ser)
data=np.array(['a','b','c','d'])
ser=pd.Series(data)
print("panda series from numpy array",ser)
calories={"day1": 420,"day2" : 380,"day3"  : 390}
myvar=pd.Series(calories,index=["day1","day2"])
print(myvar)