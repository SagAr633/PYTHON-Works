a={1,2,3,4,5}
b={1,3,5,7}
c=set()
for i in a:
    if i in b:
        c.add(i)
print(c)