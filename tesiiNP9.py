#write a sum of 2 number using numpy
import numpy as np
#get=np.array([34,76,36,27,18,98,12,45,9,29])

#for i in range(len(get)):
   # print(i)
#met=np.array([67,89,99])
#if get.shape==met.shape:
 #   print(get+met)
#else:
 #   print("array not same shape")

#j=0
#while not 1<=j and 100>j:
 #   j=int(input("enter the number"))
   # if not 1<=j and 100>j:
    #    print("invalid number please enter again")
#print("vaild number",j)

for i in range (3):
    x=int(input("enter the number"))
    if x>1 and x<100:
        print("vaild number ",x)
        break
    else:
        print("invaild number",x)
        
    