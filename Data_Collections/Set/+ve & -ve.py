s={1,-2,3,-6,6,-4,9,9,-10}
Pos=set()
Neg=set()
for i in s:
    if i>0:
        Pos.add(i)
    else:
        Neg.add(i)
print(Pos)
print(Neg)