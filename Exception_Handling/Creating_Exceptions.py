num=int(input('enter num1'))
if num>=0:
    print(num)
else:
    raise Exception('Number Is Negative')
#raise is used here to create our own exception.