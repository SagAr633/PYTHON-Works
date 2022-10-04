def add(n1,n2):
    return n1+n2
def sum(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
while True:
    options=input('1.add\n2.sum\n3.mul\n4.div\n5.stop')
    if options=='5':
        break
    else:
        if options in '1234':
            n1=int(input('Number 1'))
            n2=int(input('Number 2'))
            if options=='1':
                print(add(n1,n2))
            elif options=='2':
                print(sum(n1,n2))
            elif options=='3':
                print(mul(n1,n2))
            elif options=='4':
                print(div(n1,n2))
        else:
            print('Invalid Option')



