# def recfibo(n): #n=0,1,2,3,4,5,6,7,8,9
#     if n<=1: #n=0-true , n=1-true, n=2-false-move to else
#         return n
#     else:
#         return recfibo(n-1)+recfibo(n-2)
#         #n-1 means the number before n
#         #n-2 means two numbers before n
#         #n=2-recfibo(n-1=2-1=1)+recfino(n-2=2-2=0)=1
#         #n=3-recfibo(n-1=1)+recfibo(n-2=1)=2
#         #n=4-recfibo(n-1=2)+recfibo(n-2=1)=3
# for i in range(10):
#     print(recfibo(i))
# #recfibo(0)=0
# #recfibo(1)=1
# #recfibo(2)=1
# #recfibo(3)=2
# #recfibo(4)=3
# #recfibo(5)=5
# #recfibo(6)=8
# #recfibo(7)=13
# #recfibo(8)=21
# #recfibo(9)=34
#
#
#

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
for i in range(15):
    print(fibo(i))

a=6
for i in range(6):
    for l in range (a):
        print(end=' ')
    a-=1
    for j in range(i):
        print('^',end=' ')
    print()






def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
for i in range(10):
    print(fibo(i))

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Parent(Person):
    def __init__(self,name,age,place,kids,name_of_husband):
        super().__init__(name,age,place)
        self.kids=kids
        self.name_of_husband=name_of_husband
class Employee(Parent):
    def __init__(self,name,age,place,kids,name_of_husband,company,salary,experience):
        super().__init__(name,age,place,kids,name_of_husband)
        self.company=company
        self.salary=salary
        self.experience=experience

    def printvalue(self):
        print('Name :',self.name, 'Age : ',self.age,'Place : ',self.place,'Kids : ',self.kids,
              'Spouse : ',self.name_of_husband,'Company Name : ',self.company,'Salary : ',self.salary,
              'Years of Experience : ',self.experience)

a1=Employee('Anu',33,'Calicut',2,'Arjun','TCS',50000,'5-Years')
a1.printvalue()


ab=10
for i in range(10):
    for l in range(ab):
        print(end=' ')
    # ab-=1
    for j in range(l):
        print('$',end=' ')
    print()


def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num-1)

print(fact(5))

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
for i in range(10):
    print(fib(i))

# def arm(n):
#     for i in n:
#         if i**3 == n:
#             return 'armstrong'
#         else:
#             return 'not an armstrong'
# print(arm(153))

num12=input('enter number')
for i in num12:
    if i*len(str(num12))==num12:
        print('armstrng')
    else:
        print('not')