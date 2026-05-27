# average of an array without use function
import numpy as np
arr=np.array([12,5,62,87])
total=0
for i in range(len(arr)):
    total=total+arr[i]
avg=total/len(arr)
print("sum of array=",total)
print("average of array=",avg)