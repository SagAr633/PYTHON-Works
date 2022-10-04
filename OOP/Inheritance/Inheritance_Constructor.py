class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printper(self):
        print(self.name,self.age,self.place)
class Student(Person):
    def __init__(self,roll_no,dep,college,name,age,place):
        super().__init__(name, age, place)
        self.roll_no=roll_no
        self.dep=dep
        self.college=college
    def printstudent(self):
        print(self.name,self.age,self.place)
        print(self.roll_no,self.dep,self.college)
a1=Student(420,'CSE','XYZ','Sagar',26,'Calicut')
a1.printstudent()