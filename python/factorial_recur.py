def fct(a):
    return 1 if (a==0) else a*fct(a-1)
a=int(input("Enter number:"))
print(fct(a))


