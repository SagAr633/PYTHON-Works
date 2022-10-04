# [list]
l1 = ['abc', 123, 'zx9', 999]
l1.append('sagar')
l1.insert(1, 'max')
l1.remove(999)
l1.pop(2)
print(len(l1))
print(l1)
print(l1[::-1])
print(l1[0:2])
# (tuple)
l3 = ('dom', 99, 'sagar', -88, 'python')
l4 = ('django',)
print(l3 + l4)

# {set}
l5 = {'sql', 997, -789, 'add', 'remove'}
l5.add('pop')
l5.remove('remove')
l5.pop()
print(l5)
# dictionary
dic1 = {'name': 'sagar', 'place': 'calicut'}
dic2 = [{'name': 'sagar'}, {'name': 'arun'}, {'name': 'john'}]
dic1.update({'age': 26})
print(dic1)
print(dic1['name'], dic1['place'], dic1['age'])
print(dic2[2]['name'])

l2 = 'malayalam'
if l2 == l2[::-1]:
    print('palindrom')
else:
    print('not a palindrom')

z = [32, 22, 9, 2, 6, 7, 5, 8, 44, 53, 98, 16, -2, -12]
a = [i for i in z if i > 0 and i % 2 == 0]
b = [i for i in z if i > 0 and i % 2 != 0]
print(a)
print(b)
