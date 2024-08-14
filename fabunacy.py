def febunacy(n):
    a,b=0,1
    while(n!=1):
        c=a+b
        a=b
        b=c
        n=n-1
    return b
n = int(input("enter the number: "))
m = febunacy(n-1)
print("fab=",m)
