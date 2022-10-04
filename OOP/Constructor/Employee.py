class Employee:
    company_name = 'GOOGLE'

    def __init__(self, name, id, designation, salary):
        self.name = name
        self.id = id
        self.designation = designation
        self.salary = salary

    def empprint(self):
        print('Company_Name ::', Employee.company_name)
        print("Name ::", self.name)
        print('Employee_ID ::', self.id)
        print('Designation ::', self.designation)
        print('Salary ::', self.salary)


em1 = Employee('Sagar', 4324, 'Developer', 50000)
em1.empprint()
