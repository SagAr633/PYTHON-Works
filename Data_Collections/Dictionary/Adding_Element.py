# Empty Dictionary
dic1={}
dic2={}
print(dic1)
print(type(dic1))
# Method 1
dic1.update({1:'AR',2:'SMG'})
print(dic1)
# Method 2 - can only add one element at a code
dic2[1]='SMG'
dic2[3]='SNIPER'
print(dic2)

dic3=[
    {'name':'sagar'},
    {'name':'arun'},
     {'name':'sam'}
]
print(dic3[1]['name'])