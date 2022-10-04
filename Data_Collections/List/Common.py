l1=[1,2,3,4,5]
l2=[3,4,5,6,7]

# for i in l1:
#     if i in l2:
#         print(i)

print(list(set(l1).intersection(set(l2))))