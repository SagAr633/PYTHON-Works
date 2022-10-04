# find second minimum element

list1=[3,5,1,8,6,9,4,2,7]
list1.sort()
print(list1[1])

# if there is any duplication

list2=[2,3,5,23,54,4,2,3,5,9,7,4]
list2.sort()
a=list(set(list2))
print(a)
print(a[1])