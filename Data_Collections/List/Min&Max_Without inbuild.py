l=[3,7,5,4,8,6]
min=l[0]
max=l[0]
for i in l:
    if i<min:
        min=i
    elif i>max:
        max=i
print(min,max)