import math
n = int(input("enter the n: "))
k=n
add = 0
while(n!=0):
    r=n%10
    m = math.factorial(r)
    add += m
    n=n//10
print(add)
if(k==add):
    print("strong")
else:
    print("it is not a strong number ")
