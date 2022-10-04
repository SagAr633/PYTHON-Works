num=1,2,3,4,5,6,7,8,9

count_odd=0
count_even=0

for a in num:
    if not a%2==0:
        count_even+=1
    else:
        count_odd+=1
print('No.of Even Numbers',count_even)
print('No.of Odd Numbers',count_odd)