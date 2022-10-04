t=tuple('im a fucking asshole')
# print(type(t))
i=t.index('g')
print(i)
# lenght of a tuple
t2=tuple('im a fucking asshole')
d= len(t2)
print(d)
# tuple to dict
t3=tuple('adnijshdi')
# unzip tuple
t4=[(121,232),(343,'sdd'),(223,'ere')]
print(list(zip(*t4)))
# reverse tuple
t5=tuple('123njbhjb456')
q=t5[::-1]
print(q)
# remove empty tuple
t6=[(),(),('',),('a','b'),('a','b','c'),('d')]
z=[i for i in t6 if i]
print(z)
# sort a tuple
t7=[('item1','12.20'),('item2','15.10'),('item3','24.5')]
print(sorted(t7))