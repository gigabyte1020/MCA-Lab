a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("1.Addition  \n2. Subtraction \n3.Multiplication \n4.Division")
ch=int(input("Enter choice: "))
if ch==1:
    print ("Sum is ",a+b)
elif ch==2:
    print("Difference is ",a-b)
elif ch==3:
    print ("Product is ",a*b)
elif ch==4:
    print("Quotient is ",a/b)
else:
    print("Error")

    

