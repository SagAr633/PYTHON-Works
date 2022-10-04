print(7*'*','Collatz Conjecture',7*'*')
# user=int(input('Enter a Number'))
b=[]
def coltz(n):
    global user
    for i in range(1,100):
        if n%2==0:
            return n/2
        else:
            return n*3+1
    print(coltz(20))