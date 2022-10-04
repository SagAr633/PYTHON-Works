


l=[3,5,9,7]
cube=list(map(lambda n:n**3,l))
print(cube)
square=list(map(lambda n:n**2,l))
print(square)

#print all names in uppercase
names=['django','flask','oodo','spring']
upcase=map(lambda name:name.upper(),names)
print(list(upcase))

#terminal function
n=3
print('+ve' if n>0 else '-ve')
n1=3
n2=8
print(n1 if n1>n2 else n2)

#create a new list from lst if num<5 map to num-1 if num>5 map to num+1
lst=[2,3,6,7,8,4]
out=map(lambda n:n-1 if n<5 else n+1,lst)
print(list(out))
