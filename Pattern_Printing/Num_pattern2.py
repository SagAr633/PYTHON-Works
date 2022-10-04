for i in range(5):
    for j in range(i):
        print(j,end=' ')
    print()

for i in range(5):
    for j in range(i):
        print(i,end=' ')
    print()

for i in range(8):
    for j in range(i):
        print(i*j,end=' ')
    print()


name='sagar'
str='my name is {}'
print(str.format(name))