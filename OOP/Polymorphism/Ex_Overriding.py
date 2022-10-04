class Parent:
    def setpar(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print('1',self.n1+n2)
class Child(Parent):
    def setpar(self,no1,no2):
        self.no1=no1
        self.no2=no2
        print('2',self.no1+no2)
class SecondChild(Child):
    def setpar(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print('3',self.num1+num2)
a=SecondChild()
a.setpar(4,5)