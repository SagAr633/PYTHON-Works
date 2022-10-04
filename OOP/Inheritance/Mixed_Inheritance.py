class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printper(self):
        print(self.name,self.age,self.place)
class Child(Person): #single_level_Inheritance
    def setchild(self,school,std,dob):
        self.school=school
        self.std=std
        self.dob=dob
    def printchild(self):
        print(self.school,self.std,self.dob)
class Parent:
    def setparent(self,adress,mob_no):
        self.adress=adress
        self.mob_no=mob_no
    def printparent(self):
        print(self.adress,self.mob_no)
class Student(Child): #Multi_level_Inheritance
    def setstudent(self,roll_no,dep):
        self.roll_no=roll_no
        self.dep=dep
    def printstudent(self):
        print(self.roll_no,self.dep)
class Employee(Person,Parent): #Multiple_Inheritance
    def setemp(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
    def printemp(self):
        print(self.id,self.desig,self.salary)
a1=Employee()
a1.setperson('Sagar',26,'Calicut')
a1.setparent('XYZ',7907763336)
a1.setemp(420,'Developer',50000)
a1.printper()
a1.printparent()
a1.printemp()
a2=Student()
a2.setperson('John',25,'Kochi')
a2.setchild('St.Josephs','10th_Std',1996)
a2.setstudent(123,'CSE')
a2.printper()
a2.printchild()
a2.printstudent()