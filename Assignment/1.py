s=input('enter string')
v='aeiou'
x=''
for i in s:
    if i not in v:
        x=x+i
print(x)