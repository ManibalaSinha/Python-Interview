a =[1,2,2,3,4,4,5]
#a = list(set(a))
res=[]
[res.append(val) for val in a if val not in res]
print(res)