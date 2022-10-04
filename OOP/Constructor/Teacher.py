class Teacher:
    college_name='ABCDX'
    def __init__(self,name,id,dep,sub):
        self.name=name
        self.id=id
        self.dep=dep
        self.sub=sub
    def printt(self):
        print(Teacher.college_name,self.name,self.id,self.dep,self.sub)

t1=Teacher('Salih',420,'XXX','Enthum')
t1.print()

#department = to initial instance variable while creating object