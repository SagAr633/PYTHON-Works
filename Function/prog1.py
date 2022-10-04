x=int(input('Enter Initial range'))
y=int(input('Enter Final range'))
for a in range(x,y+1):
    for i in range(2,a):
        if a%i==0:
            break
    else:
        print(a)













