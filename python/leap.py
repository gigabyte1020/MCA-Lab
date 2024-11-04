year=int(input("Enter year:"))
if year%400==0:
    print(year," is a leap year")
elif year%100==0:
    print("NO")
elif year%4==0:
    print("YES")
else:
    print("NO")
    
    
