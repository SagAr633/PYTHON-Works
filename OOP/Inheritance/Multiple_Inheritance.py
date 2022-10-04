# Multiple Inheritance
   #child class have more than one parent class

class A:
    def methodA(self):
        print('Inside A')
class B:
    def methodB(self):
        print('Inside B')
class C(A,B):
    def methodC(self):
        print('Inside C')

c=C()
c.methodA()
c.methodB()
c.methodC()