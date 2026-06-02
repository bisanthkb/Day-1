l=[1,1,2,3,3,3,1,2,4,5,6]
res=[]
for i in l:
    if i not in res:
        res.append(i)
print(res)