s='Luminar Technolab'

user=input('Enter a Letter')
new=''
for i in s:
    if i not in user:
        new=new+i
print(new)
