import math
def area_triangle(a,b,c):
    s=(a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
r=int(input("enter the side 1:"))
t=int(input("enter the side 2:"))
y=int(input("enter the side 3:"))
print("area of triangle=",area_triangle(r,t,y))