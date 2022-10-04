#function call function itself
# a=5
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)

def recfact(n):
    if n==1: #(1 is the stopping point here)
        return 1#(return value shouldnt be 0 in factorial case)

    else:
        return n*recfact(n-1)   #5*recfact(4)
                               # 4*recfact(3)
                               # 3*recfact(2)
                              # 2*recfact(1)
                              # 1
print(recfact(5))