class Person:
    def info(self, name, age, place, marital_status):
        self.name = name
        self.age = age
        self.place = place
        self.marital_status = marital_status


class Employee(Person):
    def emp_info(self, company_name, designation, experience, salary):
        self.company_name = company_name
        self.designation = designation
        self.experience = experience
        self.salary = salary

    def printemp(self):
        print(self.name, self.age, self.marital_status, self.place, self.company_name, self.designation,
              self.experience, self.salary)


a1 = Employee()
a1.info('sagar', 26, 'single', 'calicut')
a1.emp_info('xyz', 'developer', '5 Years', '40k')
a1.printemp()


class Person1:
    def __init__(self, name, age, place, country):
        self.name = name
        self.age = age
        self.place = place
        self.country = country


class Student(Person1):
    def __init__(self, name, age, place, country, school, std, roll_no):
        super().__init__(name, age, place, country)
        self.school = school
        self.std = std
        self.roll_no = roll_no

    def printall(self):
        print(self.name, self.age, self.place, self.country,
              self.school, self.std, self.roll_no)


a1 = Student('sagar', 15, 'calicut', 'india', 'st.josephs', '10th', 42)
a1.printall()
