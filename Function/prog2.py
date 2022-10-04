# def prime(initial,final):
#     return 'n'
# initial=int(input('Enter Initial'))
# final=int(input('Enter Final'))
# for n in range(initial,final+1):
#     for i in range(2,n):
#         if n%i==0:
#             break
#     else:
#         print(n)

def primecheck(initial,final):
    for num in range(initial,final+1):
        for i in range(2,num):
            if num%i==0:
                break
        else:
             print(num)
primecheck(1,11)

