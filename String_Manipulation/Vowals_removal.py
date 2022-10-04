user=input('Enter a Word')
v='aeiou'
new=''
for i in user:
    if i not in v:
        new=new+i
print(new)