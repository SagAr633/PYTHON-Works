s=input('Enter String')
count={}
data=s.split(' ')
# print(data)
for word in data:
    if word not in count:
        count.update({word:1})
    else:
        val=count[word]
        val+=1
        count.update({word:val})
print(count)
