#write a python program to find a largest number in an array using loop without built in function
import numpy as np
ig=np.array([270,456,287,56,812,394])
largest=ig[0]
smallest=ig[0]
for i in range(1,len(ig)-1):
    if(largest<ig[i]):
        largest=ig[i]
        iaposition=i
for j in range(1,len(ig)-1):
    if(smallest>ig[j]):
        smallest=ig[j]
        position=j
print("largest=",ig)
print(" bioggest index position=",iaposition)
print("smallest  index position=",position)
