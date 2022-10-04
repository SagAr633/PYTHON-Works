class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printperson(self):
        print(self.name,self.age,self.place)
class Student(Person):
    def setstudent(self,rollno,department):
        self.rollno=rollno
        self.department=department
    def printstudent(self):
        print(self.name,self.age,self.place,self.department,'Roll_No::',self.rollno)
s1=Student()
s1.setperson('Sagar',26,'Calicut')
s1.setstudent(46,'CSE')
s1.printstudent()
# s1.printperson()
