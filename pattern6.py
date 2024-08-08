n = int(input("enter the n: "))
for i in range(1,n+1):
    print()
    for j in range(i):
        print(" ",end='')
    for k in range(1,n+1):
        print("*",end='')