l=[1,2,3,4,5,6,7,8,9,10]
Prime=[]
Non_prime=[]
for num in l:
    for i in range(2,num):
        if num % i == 0:
            Non_prime.append(num)
            break
    else:
        Prime.append(num)
print(Prime)
print(Non_prime)



l1=[22,43,65,3,56,876,12,356]
prime=[]
non_prime=[]
for num in l1:
    for i in range(2,num):
        if num % i == 0:
            non_prime.append(num)
            break
    else:
        prime.append(num)

print(prime)
print(non_prime)