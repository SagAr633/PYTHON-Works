# use list comprehension to create a list with
# elements 1-100 that are divisible by 5

l=[i for i in range(1,100+1) if i%5==0]
print(l)