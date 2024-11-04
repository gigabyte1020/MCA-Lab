import math
a=int(input("Enter number:"))
b=int(input("Enter number:"))
c=int(input("Enter number:"))
d=b*b-4*a*c
if d>0:
    root1=((-b)+math.sqrt(d))/(2*a)
    root2=((-b)-math.sqrt(d))/(2*a)
    print(root1)
    print(root2)

elif d==0:
    root1=((-b)+math.sqrt(d))/(2*a)
    print(root1)
else:
    print("No real root")

