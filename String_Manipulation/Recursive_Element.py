s=input('enter a word')
b=''
for i in s:
    if i not in b:
        b=b+i #b+=i
    else:
        print(i)
        break