score=int(input('Enter Score'))

if score>=90:
    print('Your Grade Is A+')
elif score>=80 and score<90:
    print('Your Grade Is A')
elif score>=70 and score<80:
    print('Your Grade Is B+')
elif score>=60 and score<70:
    print('Your Grade Is B')
elif score>=50 and score<60:
    print('Your Grade Is C+')
else:
    print('You Are Faild')