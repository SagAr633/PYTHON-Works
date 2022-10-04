# Multi_level Inheritance

class A:
    def methodA(self):
        print('inside method A')
class B(A):
    def methodB(self):
        print('inside method B')
class C(B):
    def methodC(self):
        print('inside method C')

o=C()
o.methodC()
o.methodB()
o.methodA()