#instance variable= call variable using self.
# static variable= call varible using class name
class Student:
    college_name='XYZ' #Static Varialbe
    def setstudent(self,name,roll_no,department):
        self.name=name
        self.roll_no=roll_no
        self.department=department
    def printstudent(self):
        print(self.name,self.roll_no,self.department,Student.college_name)

stu1=Student()
stu1.setstudent('Sagar',46,'CE')
stu1.printstudent()
stu2=Student()
stu2.setstudent('Anu',12,'ECE')
stu2.printstudent()