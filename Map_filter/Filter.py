lst=[2,3,6,7,8,4]

even=filter(lambda n:n%2==0,lst)
print(list(even))

odd=filter(lambda n:n%2!=0,lst)
print(list(odd))

lst.sort(reverse=True)
print(lst)

#sort is an
#sorted is a function