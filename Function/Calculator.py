def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
while True:
    option=input('Select Option \n1.add \n2.sub \n3.mul \n4.div \n5.stop')
    if option=='5':
        break
    else:
        if option in '1234':
            num1=int(input('Enter Num1'))
            num2=int(input('Enter Num2'))
            if option=='1':
                print(add(num1,num2))
            elif option=='2':
                print(sub(num1,num2))
            elif option=='3':
                print(mul(num1,num2))
            elif option=='4':
                print(div(num1,num2))
        else:
            print('Invalid Option')