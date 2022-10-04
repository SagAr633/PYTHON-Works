s={1,2,43,5,65,23,12,65,87}
odd=set()
even=set()

for i in s:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print(odd,even)
