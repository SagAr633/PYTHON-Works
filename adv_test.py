# class Vehicle:
#     def vehinfo(self,brand,model,manu_year):
#         self.brand=brand
#         self.model=model
#         self.manu_year=manu_year
# class Bus(Vehicle):
#     def regi(self,registration_no):
#         self.registration_no=registration_no
#     def print_veh(self):
#         print(self.brand,self.model,self.manu_year,self.registration_no)
# a1=Bus()
# a1.vehinfo('Hyundai','Verna',2020)
# a1.regi('KL11BB007')
# a1.print_veh()

# class Person:
#     def setperson(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place
#     def printperson(self):
#         print(self.name,self.age,self.place)
# class Employee(Person):
#     def setemp(self,id,designation,salary):
#         self.id=id
#         self.designation=designation
#         self.salary=salary
#     def printemp(self):
#         print(self.id,self.designation,self.salary)
# class Loan_Details(Employee):
#     def setloan(self,ref_no,amnt):
#         self.ref_no=ref_no
#         self.amnt=amnt
#     def printloan(self):
#         print(self.ref_no,self.amnt)
# class Approved_loan():
#     def app_loan(self,approved,repay):
#         self.approved=approved
#         self.repay=repay
#     def printapp(self):
#         print(self.approved,self.repay)
# class Emi(Person,Approved_loan):
#     def setemi(self,emi_amnt,duration):
#         self.emi_amnt=emi_amnt
#         self.duration=duration
#     def printemi(self):
#         print(self.emi_amnt,self.duration)
# a1=Loan_Details()
# a1.setperson('Sagar',26,'Calicut')
# a1.setemp(444,'Developer',40000)
# a1.setloan(8667644,'5_lakh')
# a1.printperson()
# a1.printemp()
# a1.printloan()
# a2=Emi()
# a2.app_loan('Your loan has been approved','Repay it on time')
# a2.setemi(20000,'4_Years')
# a2.printapp()
# a2.printemi()

# class Animal():
#     def __init__(self,breed,colour):
#         self.breed=breed
#         self.colour=colour
#     def printani(self):
#         print(self.breed,self.colour)
# class Dog(Animal):
#     def __init__(self,name,age,breed,colour):
#         super().__init__(breed,colour)
#         self.age=age
#         self.name=name
#     def printdog(self):
#         print(self.name,self.breed,self.age,self.colour)
# a1=Dog('Duffy','Pug',5,'Brown')
# a1.printdog()

import re
rule='[a][\d]{5}[b]'
s=input('Enter string')
# s='a12345b'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('Valid')
else:
    print('Not_Valid')

def valid(func):
    def wrapper(a):
        if a=='+911294567890':
            return func(a)
        else:
            raise Exception('Not Allowed')
    return wrapper
@valid
def change_number(phn_number):
    new_number=phn_number
    return new_number
print(change_number('+911294567890'))


