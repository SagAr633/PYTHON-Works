class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printper(self):
        print(self.name,self.age,self.place)
class Child:
    def __init__(self,std,school):
        self.std=std
        self.school=school
    def printchild(self):
        print(self.std,self.school)
class Student(Person,Child):
    def __init__(self,rollno,deprt,name,age,place,std,school):
        Person.__init__(self,name,age,place)
        Child.__init__(self,std,school)
        self.rollno=rollno
        self.deprt=deprt
    def printstu(self):
        print(self.rollno,self.deprt)
st=Student(42,'CSE','Akhil',24,'Calicut',12,'St.Jo')
st.printper()
st.printchild()
st.printstu()