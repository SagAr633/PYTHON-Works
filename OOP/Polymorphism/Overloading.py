#Overloading
#Same method name and different no of arguments.
class Sum:
    def findsum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
class Add(Sum):
    def findsum(self,no1,no2,no3):
        self.no1=no1
        self.no2=no2
        self.no3=no3
        print(self.no1+self.no2+self.no3)
add1=Add()
add1.findsum(2,7)

#python doesn't support overloading but it do support
#the argument on the child class