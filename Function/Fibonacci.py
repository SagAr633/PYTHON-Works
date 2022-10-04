# n1=0
# n2=1
# for i in range(10):
#     print(n1)
#     x=n1+n2
#     n1=n2
#     n2=x
#
# n1=0
# n2=1
# i=0
# while i<10:
#     print(n1)
#     x=n1+n2
#     n1=n2
#     n2=x
#     i=i+1

# nthterm=int(input('enter count'))
# n1=0
# n2=1
# i=0
# while i<nthterm:
#     print(n1)
#     x=n1+n2
#     n1=n2
#     n2=x
#     i=i+1

# def fibonacci(nterm):
#     n1=0
#     n2=1
#     i=0
#     while i<nterm:
#         print(n1)
#         x=n1+n2
#         n1=n2
#         n2=x
#         i+=1
# ntrem=int(input('enter count'))
# fibonacci(ntrem)


n1=0
n2=1
for i in range(20):
    print(n1)
    z=n1+n2
    n1=n2
    n2=z

def fibo(n):
    n1=0
    n2=1
    i=0
    while i>n:
        print(n1)
        x=n1+n2
        n2=x
fibo(20)