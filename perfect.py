n = int(input("enter the n: "))
sum=0
for j in range(1,n):
     if(n%j==0):
        sum+=j
print(sum)
if(sum==n):
    print("it is a perfect")
else:
    print("not perfect")

