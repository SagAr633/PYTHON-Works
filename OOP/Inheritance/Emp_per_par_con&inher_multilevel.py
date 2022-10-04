class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printper(self):
        print(self.name,self.age,self.place)
class Parent(Person):
    def __init__(self,adress,mob_no,name,age,place):
        super().__init__(name,age,place)
        self.adress=adress
        self.mob_no=mob_no
    def printpar(self):
        print(self.adress,self.mob_no)
class Employee(Parent):
    def __init__(self,id,desig,salary,name,age,place,adress,mob_no):
        Parent.__init__(self,name,age,place,adress,mob_no)
        self.id=id
        self.desig=desig
        self.salary=salary
    def printemp(self):
        print(self.id,self.desig,self.salary)
em=Employee(420,'Developer',50000,'Sagar',26,'Calicut','XYZ',7907763336)
em.printper()
em.printpar()
em.printemp()
