f=open('Example.txt','r')
print(f)
for i in f:
    print(i)
    a=i.rstrip('\n') # rstrip removes the empty line b/w two words
    print(a)