# QUEUE
# Fifo first in first out
# enqueue = Add elements like people in a queue one after another
# dequeue = Remove element- first element in the queue is the one to remove
stack=[]
size=int(input('Enter Size'))
x=0
def enqueue():
    global x,size
    if x>=size:
        print('Stack Is Full MF')
    else:
        element=int(input('Enter Element'))
        stack.append(element)
        x+=1
        print(stack)
def dequeue():
    global x,size
    if x<=0:
        print('Stack Is Empty MF')
    else:
        dequeue(0)
        print(stack)
        x -= 1
while True:
    operations=int(input('Select Operations \n1.Enqueue \n2.Dequeue'))
    if operations==1:
        enqueue()
    elif operations==2:
        dequeue()
    else:
        print('Invalid Operation...Select Either 1 or 2')