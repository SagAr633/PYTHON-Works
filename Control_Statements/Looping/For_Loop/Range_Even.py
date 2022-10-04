# 5 to 15 even number 6,8,10,12,14

# for a in range(5,15+1):
#     if a%2==0:
#         print(a)

initial=int(input('enter initial range'))
final=int(input('enter final range'))
for a in range(initial,final+1):
    if a%2==0:
        print(a)

