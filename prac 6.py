word=input('Enter The Word')
i=b=0
for a in word:
    if a.isdigit():
        i=i+1
    elif a.isalpha():
        b=b+1
    else:
        pass
print('Letter',b)
print('Digits',i)


