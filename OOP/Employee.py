class Employee:
    company_name='XYZ'
    def setemplo(self,name,id,desig,salary):
        self.name=name
        self.id=id
        self.desig=desig
        self.salary=salary
    def printemp(self):
        print('Employee_Name::',self.name)
        print('ID::',self.id)
        print('Designation::',self.desig)
        print('Salary::',self.desig)
        print('Company_Name::',Employee.company_name)

emp1=Employee()
emp1.setemplo('Sagar',3245,'Developer',50000)
emp1.printemp()