class Student:
    def __init__(self,name,roll_no,deprt,score):
        self.name=name
        self.roll_no=roll_no
        self.deprt=deprt
        self.score=score
    def printStu(self):
        print(self.name,self.roll_no,self.deprt,self.score)
f=open('Student.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    name=data[0]
    roll_no=data[1]
    deprt=data[2]
    score=data[3]
    st=Student(name,roll_no,deprt,score)
    st.printStu()