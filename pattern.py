n = int(input("enter the n: "))
m=n
for i in range(1,n+1,2):
    print()
    for k in range(m,0,-1):
        print(" ",end='')
    for j in range(i):
        print("*",end='')
    m=m-1
r=n
if(n%2!=0):
    l=n
else:
    l=n-1
for i in range(l-2,0,-2):
    print()
    for k in range(m,r+1,1):
        print(" ",end='')
    for j in range(i):
        print("*",end='')
    r=r+1