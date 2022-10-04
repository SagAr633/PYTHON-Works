# Recursive Fibonacci
def rfib(a):
    if a<=1:
        return a
    else:
        return rfib(a-1)+rfib(a-2)
for i in range(5):
    print(rfib(i))

# Recursive Factorial
def recfac(n):
    if n==1:
        return n
    else:
        return n*recfac(n-1)
print(recfac(5))

# Recursive Prime Numbers
def recnat(n):
    if n==0:
        return 0
    else:
        return n+recnat(n-1)
print(recnat(10))