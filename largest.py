num=[]
lar=0
n=int(input("Enter the number of elements you want in the list: "))
for i in range(1,n+1):
    element=int(input("Enter the element of %d element:" %i))
    num.append(element)
for j in range(1,n):
    if num[j]>lar:
        lar=num[j]  
print("The largest element in the list is:",lar)
