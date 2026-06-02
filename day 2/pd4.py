n=int(input("enter the number:"))
count=0
res=0
s=str(n)
l=len(s)
k=int(l)
i=1
while n:
    d=n%10
    if i<k+1:
        res=res+d**i
        i+=1
    n=n//10
print(res)