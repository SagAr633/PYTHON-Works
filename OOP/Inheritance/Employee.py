class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Employee(Person):
    def setemployee(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
    def printemployee(self):
        print(self.name,self.age,self.place,self.id,self.desig,self.salary)
e1=Employee()
e1.setperson('Rahul',25,'Calicut')
e1.setemployee(420,'Developer',50000)
e1.printemployee()