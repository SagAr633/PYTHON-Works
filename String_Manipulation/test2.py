# tup1 = ('sagar', 26)
# tup2 = ('calicut',)
# print(tup1 + tup2)
#
# # s=input('enter a word')
# # if s == s[::-1]:
# #     print('palindrome')
# # else:
# #     print('not a palindrome')
#
# l = ['sagar', 26, 'calicut']
# l.insert(2, 'dev')
# print(l)
#
#
# def fact(num):
#     if num <= 1:
#         return num
#     else:
#         return num * fact(num - 1)
#
#
# print(fact(5))
#
#
# def nat(no):
#     if no <= 1:
#         return no
#     else:
#         return no + nat(no - 1)
#
#
# print(nat(5))
#
#
# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n - 1) + fibo(n - 2)
#
#
# for i in range(10):
#     print(fibo(i))
#
# rows = 8
# space = 10
# for i in range(rows):
#     for l in range(space):
#         print(end=' ')
#     space -= 1
#     for j in range(i):
#         print('*', end=' ')
#     print()
# for i in range(rows, -1, -1):
#     for l in range(space, 0, -1):
#         print(end=' ')
#     space += 1
#     for j in range(i):
#         print('*', end=' ')
#     print()
#
# import re
#
# rules = '[A-Za-z0-9/w]+[@][g][m][a][i][l][.][c][o][m]'
# s = input('enter g-mail id')
# match = re.fullmatch(rules, s)
# if match is not None:
#     print('Valid')
# else:
#     print('Not Valid')
#
# da = open('data.txt', 'r')
# list1 = []
# for i in da:
#     data = i.rstrip().split(' ')
#     list1.extend(data)
# count = {}
# for i in list1:
#     if i not in count:
#         count.update({i: 1})
#     else:
#         v = count[i]
#         v += 1
#         count.update({i: v})
# print(count)
#
#
# def calculator():
#     options = int(input(['add', 'sub', 'div', 'mul']))
#     num1 = int(input('enter first number'))
#     num2 = int(input('enter second number'))
#     if options == 1:
#         return num1 + num2
#     elif options == 2:
#         return num1 - num2
#     elif options == 3:
#         return num1 * num2
#     else:
#         return num1 / num2
#
#
# print(calculator())

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


for p in range(10):
    print(fib(p))

row = 6
space = 5
for i in range(row):
    for l in range(space):
        print(end=' ')
    space -= 1
    for j in range(i):
        print('*', end=' ')
    print()


# def calculator():
#     options = int(input(['add', 'sub', 'mul', 'div']))
#     num1 = int(input('enter number 1'))
#     num2 = int(input('enter number 2'))
#     if options == 1:
#         return num1 + num2
#     elif options == 2:
#         return num1 - num2
#     elif options == 3:
#         return num1 / num2
#     else:
#         return num1 * num2
#
#
# print(calculator())

import re
rules = '[a-zA-Z0-9/w]+[@][g][m][a][i][l][.][c][o][m]'
str1 = input('enter gmail id')
match = re.fullmatch(rules,str1)
if match is not None:
    print('valid')
else:
    print('invalid')