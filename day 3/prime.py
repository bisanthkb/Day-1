n=int(input("enter the number"))
flag=0
for i in range(2,int(n**.5)+1):
    if n%i==0:
        flag=1
        break
if flag==0:
    print("prime")
else:
    print("not prime")