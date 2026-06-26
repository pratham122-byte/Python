import pandas as pd
author=['pratham','ankit','ankur']
articl=[23,45,67]
aurthor_series=pd.Series(author)
article_series=pd.Series(articl)
series objects as Values
frame=({'author':aurthor_series,'article':article_series})
Dictonary
result=pd.DataFrame(frame)
print(result)