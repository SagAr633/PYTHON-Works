# 1.Function without argument\
# s=input('enter string')
# def palindrom():
#
#     if s==s[::-1]:
#         print("palindrom")
#     else:
#         print('not palindrom')
# palindrom()

def palin(fn):
    if fn == fn[::-1]:
        print('palindrom')
    else:
        print('Not_palindrom')


palin('malayalam')


# 2.Function with argument

# def palindrom(s):
#     if s==s[::-1]:
#


# 3.Function with argumnet and return type

# def palindrom(s):
#     if s==s[::-1]:
#         return "palindrom"
#     else:
#         return "not palindrom"
# print(palindrom('malayalam'))


def palindrome(fn):
    if fn == fn[::-1]:
        print('Palindrome')
    else:
        print('Not a palindrome')


palindrome('malayalam')
