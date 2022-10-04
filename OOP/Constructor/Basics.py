#Constructor
class Student:
    college_name='AWM'
    def __init__(self,name,roll_no,departmnet):
        self.name=name
        self.roll_no=roll_no
        self.department=departmnet
    def printvalue(self):
        print(self.name,self.roll_no,self.department,Student.college_name)

s1=Student('Sagar',42,'CSE')
s1.printvalue()