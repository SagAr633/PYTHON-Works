s=input('Enter a Word')
a=''
rep=''
for i in s:
    if i not in a:
        a=a+i
    else:
        rep+=i
print('final recursive element',rep[-1])
