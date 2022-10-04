dict1={1:'a',2:'b',3:'c',4:'d',5:1,6:2,7:3}
user=int(input('Enter Key'))
if user in dict1: # or, if user in dict1.keys()
    print('Present')
else:
    print('Not_Present')
