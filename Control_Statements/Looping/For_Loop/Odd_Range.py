initial=int(input('enter initial number'))
final=int(input('enter final number'))

for i in range(initial,final+1):
    if i%2==1: # or i%2!=0
        print(i)