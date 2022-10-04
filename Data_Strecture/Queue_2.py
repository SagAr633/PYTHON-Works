queue=[]
size=int(input('Enter Size'))
front=0
rear=0
def enqueue():
    global size,front,rear
    if rear>=size:
        print('Queue is full')
    else:
        e=int(input('Enter Element'))
        queue.insert(rear,e) #insert(position,element)
        rear+=1
        for i in range(front,rear):
            print(queue[i])
def dequeue():
    global size,front,rear
    if front==rear:
        print('Queue is empty')
    else:
        front=front+1
        for i in range(front,rear):
            print(queue[i])
while True:
    options=int(input('Select Operations \n1.Enqueue \n2.Dequeue'))
    if options==1:
        enqueue()
    elif options==2:
        dequeue()