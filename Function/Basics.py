# Functions - to reuse a code using it's name
#to make it reusable
#1.Functions without arguments(use it as an input)
# def add():
#     num1=int(input('enter num 1'))
#     num2=int(input('enter num 2'))
#     print(num1+num2)
# add()
# add()
#2.Function with argument(input variable are the argument)
# def add(num1,num2):
#     sum=num1+num2
#     print(sum)
# add(32,12)
# add(23,76)
# 3.Function with arguments and return type(return can't print)
def add(num1,num2):
    return num1+num2
no1=int(input('enter'))
no2=int(input('enter'))
print(add(no1,no2))
print(add(67,34))