def nat(n):
    if n==0:
        return 0
    else:
        return n+nat(n-1)
print(nat(5))

#factorial

def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)
print(fact(5))