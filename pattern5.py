n = int(input("enter the n: "))
for i in range(1,n+1):
    print()
    for j in range(i):
        print("*",end='')
for i in range(n-1,0,-1):
    print()
    for j in range(i):
        print("*",end='')