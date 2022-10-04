# Decorators

def swap(func):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
        else:
            return func(a,b)
    return wrapper
@swap
def sub(num1,num2):
    return num1-num2
@swap
def div(num1,num2):
    return num1/num2

print(sub(24,9))
print(div(9,2))



# def substract(num1,num2):
#     if num1<num2:
#         num1,num2=num2,num1
#         return num1 - num2
#     else:
#         return num1-num2
# print(substract(17,12))