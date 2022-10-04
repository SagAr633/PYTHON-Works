l=[1,2,3,4,5,6,1,2,3,4]
d=[]

for i in l:
    if i not in d:
        d.append(i)
    else:
        print(i)