s='Sagar'
user=input('Guess the letter')
flag=0
for i in s:
    if i==user:
        flag=1
if flag==1:
    print('You Guessed It Right')
else:
    print('Wrong Guess')