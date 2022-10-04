da=open('DATA.txt','r')
l=[]
for i in da:
    words=i.rstrip().split(' ')
    l.extend(words)
count={}
for i in l:
    if i not in count:
        count.update({i:1})
    else:
        v=count[i]
        v+=1
        count.update({i:v})
print(count)
