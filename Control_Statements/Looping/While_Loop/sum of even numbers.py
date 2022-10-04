#sum of even numbers between 10 to 20

sum=0
for i in range(10,20+1):
    if i%2==0:
        sum=sum+i
print(sum)

# print positive numbers between -5 to 5

for i in range(-5,5+1):
    if i>0:
        print(i)