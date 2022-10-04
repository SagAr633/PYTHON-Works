def calculator():
    options = int(input(['sum', 'sub', 'mul', 'div']))
    n1 = int(input('Enter first number'))
    n2 = int(input('Enter second number'))


if options == 1:
    return n1 + n2
elif options == 2:
    return n1 - n2
elif options == 3:
    return n1 / n2
else:
    return n1 * n2
print(calculator())


def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


for i in range(10):
    print(fibo(i))

a = 10
for i in range(8):
    for j in range(a):
        print(end=' ')
    a -= 1
    for l in range(i):
        print('*', end=' ')
    print()


# overriding
class Phone1:
    def selectphone(self):
        print('samsung')


class Phone2(Phone1):
    def selectphone(self):
        print('iphone')


a = Phone2()
a.selectphone()

employees = [
    [10001, "ram", "qa", 25000, 2],
    [10002, "ravi", "ba", 24000, 2],
    [10006, "arjun", "devop", 25000, 2],
    [10003, "jeevan", "qa", 27000, 3],
    [10004, "jhon", "sales", 28000, 3],
    [10005, "tinu", "mrkt", 25000, 1]
]

sal = [i[-2] for i in employees]
t_sum = sum(sal)
print(t_sum)

sal2 = list(map(lambda e: e[-2], employees))
s = sum(sal2)
print(s)

m = 10
for i in range(7):
    for l in range(m):
        print(end=' ')
    m -= 1
    for j in range(i):
        print('^', end=' ')
    print()


def cal():
    options = int(input(['add', 'sub', 'mul', 'div']))


num1 = int(input('Enter 1st number'))
num2 = int(input('Enter 2nd number'))

if options == 1:
    return num1 + num2
elif options == 2:
    return num1 - num2
elif options == 3:
    return num1 / num2
else:
    return num1 * num2
print(cal())

rows = 8
space = 10
for i in range(rows):
    for l in range(space):
        print(end=' ')
    space -= 1
    for j in range(i):
        print('*', end=' ')
    print()
for i in range(rows, -1, -1):
    for l in range(space, 0, -1):
        print(end=' ')
    space += 1
    for j in range(i):
        print('^', end=' ')
    print()


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(10):
    print(fibonacci(i))

num = int(input('enter num'))
fact = 1
while num >= 1:
    fact = fact * num
    num -= 1
print(fact)

list = [1, 2, 3, 4, 5, 6, 7]
list.append(8)
list.extend([9, 10])
print(list)

#vowals count
s = 'luminar technolab'
c = 'a,e,i,o,u'
count = 0
for i in s:
    if i in c:
        count += 1
print(count)

#recursiveelement
ss = input('enter a word')
cc = ''
for i in ss:
    if i not in cc:
        cc = cc + i
    else:
        print(i)
    break

ll2 = [23, 433, 123, 5765, 234, 2, 4, 823, 432]
el = []

while ll2:
    minimum = ll2[0]
    for i in ll2:
        if i > minimum:
            minimum = i
    el.append(minimum)
print(el)

r1 = 7
s2 = 8
for i in range(7):
    for l in range(s2):
        print(end=' ')
    s2 -= 1
    for j in range(i):
        print('*', end=' ')
    print()
