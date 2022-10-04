class Addition:
    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2
    def print(self):
        print(self.no1+self.no2)
a1=Addition(9,4)
a1.print()


class Sub:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def print(self):
        print(self.num1-self.num2)

x=Sub(84,21)
x.print()
