# set

def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)

print(sum(5))

def fib(n1):
    if n1==0 or n1==1:
        return n1
    return fib(n1-1) + fib(n1-2)

print(fib(4))

a=[1,2,3]
b=a
print(a is b,a==b)