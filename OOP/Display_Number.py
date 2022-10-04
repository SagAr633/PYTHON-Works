class Display_number:
    def get_number(self,no1,no2):
        self.no1=no1 #instance variables
        self.num2=no2 #instance variables
    def print_number(self):
        print(self.no1,self.num2)
d1=Display_number()
d1.get_number(4,7)
d1.print_number()

#Self keyword used to point to the current instance.