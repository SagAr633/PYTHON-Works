# remove letters a,b,c,d

s=input('enter string')
n=''
for i in s:
    if i not in 'abcd':
        n=n+i
print(n)
        