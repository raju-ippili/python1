def factor(n):
    s=0
    for i in range(1,n):
        if(n%i==0):
            s+=i
    return s
def perfect(n):
    m=n
    if(m==factor(n)):
        print("perfect")
    else:
        print("not perfect")
n = int(input("enter n: "))
perfect(n)
