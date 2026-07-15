import numpy as np
ig=np.array([270,456,287,56,812,394])
largest=ig[0]
for i in range(1,len(ig)-1):
    if(largest>ig[i]):
        largest=ig[i]
        iaposition=i
print("largest=",ig)
print("index position=",iaposition)