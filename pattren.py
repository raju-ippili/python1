n = int(input("enter the n: "))
m = 65
for i in range(n):
    for j in range(65,65+1+i):
        print('%c'%(m+i),end='')
    print()
    
