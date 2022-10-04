num1=int(input('num1 before swap'))
num2=int(input('num2 before swap'))


# #method_one
# temp=num1
# num1=num2
# num2=temp

#method_two
# num1,num2=num2,num1

#method_three num1=3 num2=2
num1=num1+num2 #num1=5
num2=num1-num2 #num2=3
num1=num1-num2 #num1=2

print('after swap num1=',num1)
print('after swap num2=',num2)

# tuple unpacking concept