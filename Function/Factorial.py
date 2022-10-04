#1.fucn without argument
# def factorial():
#     num = int(input('enter number'))
#     fact = 1
#     for i in range(1,num+1):
#         fact=fact*i
#     print(fact)
# factorial()

#2func with argument
# def factorial(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact=fact*i
#     print(fact)
# factorial(5)

#3.func with argument and return type

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact=fact*i
    return fact
print(factorial(5))