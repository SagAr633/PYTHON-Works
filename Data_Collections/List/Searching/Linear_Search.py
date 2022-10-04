# Linear Search

l=[1,3,6,5,9,13,42,22,65,43,99,69]
e=int(input('Enter a Number'))
f=0
for i in l:
    if i==e:
        print('Present')
        break
else:
    print('Not_Present')
# ..........................2nd method
for i in l:
    if i==e:
        f=1
        break
if f==0:
    print("Not_Present")
else:
    print('Present')

