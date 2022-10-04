stk=[]
size=int(input('Enter Size'))
top=0
def push():
    global top,size
    if top>=size:
        print('Stack Is Full')
    else:
        element=int(input('Enter Element'))
        stk.append(element)
        top=top+1
        print(stk)
def pop():
    global top,size
    if top<=0:
        print('Stack Is Empty')
    else:
        stk.pop()
        print(stk)
        top=top-1
while True:
    options=int(input('Select Option \n1.Push \n2.Pop'))
    if options==1:
       push()
    elif options==2:
        pop()
    else:
        print('Invalid Operation..Select Correct One')

