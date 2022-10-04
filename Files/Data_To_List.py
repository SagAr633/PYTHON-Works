f=open('Data.txt','r')
for i in f:
    words=i.rstrip('\n').split(' ')
    print(words)
    # print(type(words))

# f=open('Data.txt','r')
# l=[]
# for i in f:
#     words = i.rstrip('\n').split(' ')
#     l.extend(words)
# print(l)
# print(type(l))