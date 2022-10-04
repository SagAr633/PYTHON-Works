name=input('Enter Your Name')
print('Name',name)
maths=int(input('Enter Your Maths Score'))
chemistry=int(input('Enter Your Chemistry Score'))
biology=int(input('Enter Your Biology Score'))
physics=int(input('Enter Your Physics Score'))
social=int(input('Enter Your Social_Studies Score'))
english=int(input('Enter Your English Score'))
malayalam=int(input('Enter Your Malayalam Score'))
totalscore=maths+chemistry+biology+physics+social+english+malayalam
print('Total_Score = ',totalscore,'/700')
average=totalscore/7
print('Average = ',average)
if average>=95:
    print('Your Overall Grade Is A+')
elif average>=90 and average<95:
    print('Your Overall Grade Is A')
elif average>=85 and average<90:
    print('Your Overall Grade Is B+')
elif average>=80 and average<85:
    print('Your Overall Grade Is B')
elif average>=75 and average<80:
    print('Your Overall Grade Is C+')
elif average>=70 and average<75:
    print('Your Overall Grade Is C')
elif average>=65 and average<70:
    print('Your Overall Grade Is D+')
elif average>=60 and average<65:
    print('Your Overall Grade Is D')
else:
    print('We Are Sorry To Inform You That You Are Faild To Clear The Final Exams')