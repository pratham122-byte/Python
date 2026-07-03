num=[]
even=0
odd=0
n=int(input("Enter the number of elements you want in the list: "))
for i in range(1,n+1):
    element=int(input("Enter the element of %d element:" %i))
    num.append(element)
for j in range(n):
    if num[j]%2==0:
        even=even+1
        print(num[j],"is even")
    else:
        odd=odd+1
        print(num[j],"is odd")
