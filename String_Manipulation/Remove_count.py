s='Luminar Trchnolab'

d=input('enter element to remove')
count=0
for i in s:
    if i in d:
        count=count+1 #count+=1
print('count of',d,'in',s,'is',count) #or print(count)