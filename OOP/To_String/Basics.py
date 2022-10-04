# To String
# to give a value to referance that related to an object
# in To string we can only return string value
# cant't return int value(intiger or number) but it is
# possible to convert the int value to string value using str()
class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
    def __str__(self):
        return str(self.age)+self.name
per=Person('Sagar',26,'Calicut')
per.printvalue()
print(per)