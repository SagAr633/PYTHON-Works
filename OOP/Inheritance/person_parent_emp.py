class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Parent:
    def setparent(self,adress,phone_no):
        self.adress=adress
        self.phone_no=phone_no
class Employee(Person,Parent):
    def setemployee(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
    def printemp(self):
        print('Name::',self.name)
        print('Age::',self.age)
        print('Place::',self.place)
        print('Adress::',self.adress)
        print('Mob_No::',self.phone_no)
        print('ID::',self.id)
        print('Designation::',self.desig)
        print('Salary::',self.salary)
e1=Employee()
e1.setperson('Sagar',26,'Calicut')
e1.setparent('Karanthur',7907763336)
e1.setemployee(420,'Developer',50000)
e1.printemp()