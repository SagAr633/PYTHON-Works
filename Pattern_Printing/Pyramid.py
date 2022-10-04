b=9
for i in range(6):
    for a in range(b):
        print(end=' ')
    b=b-1
    for j in range(i):
        print('*',end=' ')
    print()

z=7
for c in range(7):
    for d in range(z):
        print(end=' ')
    z=z-1
    for m in range(c):
        print('^',end=' ')
    print()