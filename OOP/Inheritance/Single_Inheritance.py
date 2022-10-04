# Single Inheritance
   #single parent class for one or more child
class A: #parent class/sub class/super class
    def methodA(self):
        print('inside method A')
class B(A): #child class/sub class/derived class
    def methodB(self):
        print('inside method B')
a=A()
a.methodA()
b=B()
b.methodB()
b.methodA()