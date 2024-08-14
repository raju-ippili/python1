def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)
a = int(input("enter the number: "))
c= factorial(a)
print("factorial of %i=" %a,c,end='')
