# b=0
# for i in range(5):
#     for a in range(b):
#         print(end=' ')
#     b+=1
#     for j in range(6):
#         print('*',end=' ')
#     print()

b=5
c=1
for i in range(5):
    for a in range(b):
        print(end=' ')
    b-=1
    for j in range(c):
        print('*',end=' ')
    c+=1
    print()