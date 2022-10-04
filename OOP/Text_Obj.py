# file=open('Person.txt','r')
class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printper(self):
        print(self.name,self.age,self.place)
f=open('Person.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    name=data[0]
    age=data[1]
    place=data[2]
    pe=Person(name,age,place)
    pe.printper()
