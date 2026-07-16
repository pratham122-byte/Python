#sum of positive and negative numbers using tuples
def sum(numbers):
    pos=0
    neg=0
    for i in numbers:
        if i>=0:
            pos+=i
        else:
            neg+=i
    return(pos,neg)
number=(1,2,4,5,-6,-7,-9,5,-2)
pos,neg=sum(number)
print("sum of positive numbers:",pos)
print("sum of negative numbers:",neg)
