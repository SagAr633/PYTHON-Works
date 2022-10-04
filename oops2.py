l=lambda i:i*i
print(l(50))

class Person:
    def __init__(self,name,age,contact,place):
        self.name=name
        self.age=age
        self.contact=contact
        self.place=place
    def printper(self):
        print(self.name,self.age,self.place,self.contact)
class Student(Person):
    pass
class Teacher(Person):
    pass


st=Student('Sagar',26,"Calicut",7907763336)
tc=Teacher('Nithin',35,'Kochi',999546345)
tc.printper()
st.printper()
