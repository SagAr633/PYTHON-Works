# s='John Rambo'
# user=input('Guess the Letter')
# flag=0
# for i in s:
#     if i==user:
#         flag=1
#         break
# if flag==1:
#     print('Present')
# else:
#     print('Not Present')

    #EASY_CODE
a='John Rambo'
user= input('Guess the letter')
if user in a:
    print('Present')
else:
    print('Not Present')