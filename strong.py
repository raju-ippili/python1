def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)
def strong(n):
    result,b=0,n
    while(n!=0):
        c=n%10
        result += factorial(c)
        n=n//10
    if(b==result):
        print("strong")
    else:
        print("not strong")
n=int(input("enter n: "))
strong(n)
    
