import numpy as np
arr=np.random.randint(10,150,size=11)
print("the random array genegrated")
print(arr)
total=0
for i in range(len(arr)):
    total=total+arr[i]
avg=total/len(arr)
print(f"\n array sum={0} and average={i}".format(total,avg))
print("\n total array elements greater than average")
for i in range(len(arr)):
    if arr[i]>avg:
        print(arr[i],end=" ")