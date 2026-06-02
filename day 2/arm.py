n=int(input("enter the number"))
temp=n
count=0
arm=0
s=str(n)
l=len(s)
k=int(l)
while n:
    d=n%10
    arm=arm+d**k
    n=n//10
print(arm)


