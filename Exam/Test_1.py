min=int(input('Enter Range'))
max=int(input('Enter Range'))
for i in range(min,max):
    if i%2==0:
        for a in range(5,0,-1):
            for j in range(a):
                print(i,end=' ')
            print()
    else:
        for a in range(1,5+1):
            for j in range(a):
                print(i,end=' ')
            print()