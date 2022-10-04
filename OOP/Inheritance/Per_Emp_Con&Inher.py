class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Employee(Person):
    def __init__(self,company,id,desig,salary,name,age,place):
        super().__init__(name,age,place)
        self.company=company
        self.id=id
        self.desig=desig
        self.salary=salary
    def printem(self):
        print(self.name,self.age,self.place)
        print(self.company,self.id,self.desig,self.salary)
a1=Employee('HP',420,'Developer',50000,'Sagar',26,'Calicut')
a1.printem()