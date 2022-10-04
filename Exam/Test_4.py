# code to find the number of 'a' from a string that input by user

s=input('enter string')
count=0
for i in s:
    if i=='a':
        count+=1
print(count)