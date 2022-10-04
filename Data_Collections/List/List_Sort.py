l1=[8,5,3,1,6,9,2]
print(min(l1))
print(max(l1))
print(len(l1))
print(sum(l1))
# list1.sort()
# print(list1)
# print(list1[::-1])

l2=[3,2,6,0,8,5,4,1]
new=[]
while l2: #(loop will work until it's empty(after it goes through all elements))

    min=l2[0]
    for i in l2:
        if i<min:
            min=i
    new.append(min)
    l2.remove(min)
print(new)

l3=[5,3,7,9,1,4,0,6]
for i in l3:
    print()


l4=[312,543,578,2312,56757]
l4.sort()
print(l4)