total_score=int(input('enter score'))
if total_score<=100:
    if total_score>=90:
        print('Your Grade Is A+')
    elif total_score>=80:
        print('Your Grade Is A')
    elif total_score>=70:
        print('Your Grade Is B+')
    elif total_score>=60:
        print('Your Grade Is B')
    elif total_score>=50:
        print('Your Grade Is C+')
    else:
        print('You Are Failed')

else:
    print('Invalid Input')
