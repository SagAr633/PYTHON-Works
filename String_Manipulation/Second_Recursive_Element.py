s=input('enter string')
a=''
b=''
for i in s:
    if i not in a:
        a+=i
    else:
        if i not in b:
            b+=i
print('Second Recursive Element',b[1])