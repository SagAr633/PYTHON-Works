class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printper(self):
        print(self.name,self.age,self.place)
class Parent(Person):
    def setparent(self,adress,mob_no):
        self.adress=adress
        self.mob_no=mob_no
    def printpar(self):
        print(self.adress,self.mob_no)
class Employee(Parent):
    def setemp(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
    def printemp(self):
        print(self.name,self.age,self.place,self.adress,self.mob_no,self.id,self.desig,self.salary)
a1=Employee()
a1.setperson('Sagar',25,'Calicut')
a1.setparent('XYZ',7907763336)
a1.setemp(420,'Developer',50000)
a1.printper()
a1.printpar()
a1.printemp()