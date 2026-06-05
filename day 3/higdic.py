l=[1,3,1,3,1,2,1,4,2,2,2,2,2]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
max1=0
max2=0
for i in d:
    if d[i]>max1:
        max1=d[i]
        e=i
print(e)
