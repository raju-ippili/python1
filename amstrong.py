def count(c):
    k=0
    while(c!=0):
        #n=c%10
        k=k+1
        c=c//10
    print(k)
    return k
def power(n,m):
    p=1
    for i in range(1,m+1):
        p*=n
    return p
def amstrong(n):
    l=n
    r,d=0,0
    r=count(n)
    while(n!=0):
        m=n%10
        d+=power(m,r)
        n=n//10
    if(d==l):
        print("amstrong: ",d)
    else:
        print("not amstrong")
n= int(input("enter the n: "))
amstrong(n)
    
