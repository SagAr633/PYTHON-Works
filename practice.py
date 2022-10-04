
for a in range(1500,2700+1):
    if (a%7==0) and (a%5==0):
        print(a)

z=set('abc')
z.add('san')
z.update(set(['p','q']))
print(z)